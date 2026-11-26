# TDD with its own tests (`tdd-own`): the three evaluations

Run folder: `results/experiments/tdd-own_2026-11-19T14-38-57` (model `claude-haiku-5-5`, sampled, one sample per task). BM = ClassEval benchmark (the fixed copy, `data/ClassEval_data_fixed.json`).

## How the agent works
- Step 1: for each method, the agent gets the method's docstring (`method_description`) and the prompt "Write tests", and writes 5 tests per method (`tests_per_method: 5`, up to `test_attempts: 2` tries to get tests that load).
- Step 2: for each method, the agent gets the same docstring, the prompt "Write code" and its own tests, and runs the red/green loop (up to `max_fix_attempts: 3` fixes).
- The agent never sees `task["test"]` (the BM's tests). See `tdd-agent.md` for the full loop and what each prompt contains.

## The three evaluations

| # | Code | Tests | Classes passing every test | Tests passed |
| --- | --- | --- | --- | --- |
| 1 | Agent's code | BM's tests (`task["test"]`) | **43/100** | 1954/2196 (89.0%) |
| 2 | Agent's code | Agent's own tests | **100/100** | 2050/2050 (100.0%) |
| 3 | BM's code (`task["solution_code"]`) | Agent's own tests | **59/100** | 1917/2050 (93.5%) |

- The totals differ: 2196 are the BM's tests, 2050 are the agent's (5 per method, so 10 to 40 per class).
- Evaluation 1 went from 42 to 43 after rejecting wrong written tests (ClassEval_22, 43, 46, 48).
- On the 1480 tests both judges label `stated`, evaluation 1 gives 91/99 classes (1451/1480, 98.0%); see `results-of-insception-run-for-inconsistencies.md`.

## Correction
`project-timeline.md` step 4 earlier said the agent's tests on its own code passed 2040/2050 (99.5%). That figure cannot be reproduced: `steps/*.json` shows every method ending green, so it is **2050/2050 in all 100 classes**.

## Evaluation 3: where the BM's code fails the agent's tests
- 41 classes fail at least one own test, 133 tests in all. Per class, passed/total own tests:
  `0`: 12/20, `5`: 5/10, `7`: 9/10, `13`: 18/20, `14`: 10/30, `16`: 14/15, `17`: 26/30, `22`: 24/25, `23`: 23/25, `25`: 14/15, `26`: 13/15, `29`: 14/15, `33`: 24/25, `36`: 22/25, `38`: 11/15, `39`: 27/30, `40`: 14/15, `41`: 14/15, `44`: 12/15, `45`: 24/25, `46`: 6/10, `48`: 11/15, `53`: 8/10, `54`: 21/25, `55`: 9/10, `59`: 14/15, `61`: 35/40, `66`: 8/10, `67`: 14/15, `69`: 5/10, `71`: 13/15, `75`: 19/20, `77`: 19/20, `81`: 30/35, `89`: 17/20, `90`: 23/25, `92`: 0/20, `94`: 24/25, `97`: 9/10, `98`: 19/20, `99`: 18/20.
- **17 classes fail exactly 1 test** (7, 16, 22, 25, 29, 33, 40, 41, 45, 55, 59, 67, 75, 77, 94, 97, 98). **24 classes fail 2 or more.**
- ClassEval_92 (0/20) and ClassEval_14 (10/30) account for 40 of the 133 failing tests; ClassEval_0 fails 8.
- Reasons for the 133 failing tests (from reading them, not from a script; not rechecked since): 54 the agent assumed something the docstring does not state, 37 broken test code, 35 the docstring contradicts `task["solution_code"]`, 5 wrong example in the docstring, 2 the agent misread the docstring.

## Where the data is
- `grades/<task>.json`: evaluation 1.
- `steps/<task>.json`: evaluation 2 (the loop's own red/green steps).
- `tests_on_solution/<task>.json`: evaluation 3 (`counts`, `class_passed`, `log`).
- `tests/<task>.py`: the agent's tests.
