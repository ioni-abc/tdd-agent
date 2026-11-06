# Fixing the broken benchmark tasks (`scripts/fix_benchmark.py`)

Five tasks failed with ClassEval's own reference solution. The professor was in favour of fixing them. After the fixes the reference run gives 100/100. Decision: ADR 005.

## Diagnosing each one

The method: run the reference solution against the tests, read the failing assertion, then read the test and the code it calls.

| Task | Failing assertion | Diagnosis | Kind |
| --- | --- | --- | --- |
| 17 | `[] != [{'date': datetime(2024, 1, 2, ...)}]` | `get_upcoming_events()` compares with `datetime.now()`; the "upcoming" event is in 2024, now in the past | time bomb |
| 48 | `None != 'LAPTOP-2CS86KUM'` | reverse DNS of `0.0.0.0` returns the test author's laptop name | machine-dependent |
| 31 | `0.9819805060619655 != 0.9819805060619659` | exact float comparison; Python 3.12's `sum()` is more accurate | float precision |
| 51 | 3 `fleiss_kappa` failures | exact float comparison of NumPy results | float precision |
| 58 | `2 != 1` (sometimes) | reference solution can put two mines on one cell | flaky, solution bug |

## The fixes

| Task | Fix | Why this fix |
| --- | --- | --- |
| 17 | upcoming event moved from 2024 to 2124 | keeps the test's intent (one past event, one future event) |
| 48 | `socket.gethostbyaddr` mocked in that test | checks that `get_hostname()` returns the looked-up name, on any machine |
| 31, 51 | `assertEqual` → `assertAlmostEqual` | floats are compared to 7 decimal places, the right way to compare floats |
| 58 | **the solution** is fixed, not the test: `random.sample` picks distinct cells, capped at the number of cells | the tests are correct: `MinesweeperGame(3, 2)` promises 2 mines |

The 48 fix, inside the test:

```python
from unittest import mock
with mock.patch('socket.gethostbyaddr', return_value=('LAPTOP-2CS86KUM', [], ['0.0.0.0'])):
    result = IpUtil.get_hostname('0.0.0.0')
```

`mock.patch` replaces `socket.gethostbyaddr` only inside the `with` block, so the test no longer depends on the network or the machine.

The 58 fix:

```python
# before: two mines can land on the same cell
for num in range(self.k):
    x = random.randint(0, self.n-1)
    y = random.randint(0, self.n-1)
    arr[y][x] = 'X'

# after: k distinct cells, numbered 0 .. n*n-1, turned back into (x, y)
for cell in random.sample(range(self.n * self.n), min(self.k, self.n * self.n)):
    x, y = cell % self.n, cell // self.n
    arr[y][x] = 'X'
```

`random.sample(population, k)` picks `k` **different** items. It raises `ValueError` when `k` is larger than the population, and some tests build `MinesweeperGame(2, 5)`: 5 mines on 4 cells. The first version of the fix missed this and failed every run; `min(...)` caps it.

## Flaky tests

`ClassEval_58` passed on one day and failed the next with no code change. Running it 200 times: **47 failures**. After the fix: **0 of 500**.

- A test is **flaky** when it can pass or fail on the same code. Common causes: `random`, the current time, the network, the machine, test order.
- **One run can't show flakiness.** Run suspicious tasks many times.
- The prototype had listed 58 as broken because it happened to fail in one of its runs.
- An agent that writes the same naive mine placement will also be flaky. That is a real bug in its code, so counting it is fair.

## Fixes as data

Each fix is an entry in `data/test_fixes.json`, applied by a script, rather than a hand edit of the JSON:

```json
{
  "task_id": "ClassEval_31",
  "target": "test",
  "where": "test_correlation_coefficient_4",
  "reason": "...",
  "fix": "...",
  "old": "self.assertEqual(DataStatistics4.correlation_coefficient(...), 0.9819805060619659)",
  "new": "self.assertAlmostEqual(DataStatistics4.correlation_coefficient(...), 0.9819805060619659)",
  "count": 1
}
```

- **The file is the log** ADR 005 asks for: task, what was wrong, before/after.
- **`count`:** the script checks the old text occurs exactly that often before replacing it, and stops otherwise. A fix can never silently change nothing or the wrong place.
- **`target`:** `"test"` changes `task["test"]` and the per-method `test_code`; `"solution_code"` changes `task["solution_code"]` and the per-method `solution_code`. Both copies always change together.
- **The original is never edited:** the script writes `ClassEval_data_fixed.json`. `load_tasks()` loads the fixed copy; `load_tasks(fixed=False)` the original.
- **Reproducible:** delete the fixed file and rerun the script to get it back.
