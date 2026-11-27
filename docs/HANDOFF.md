# Handoff: the tdd-agent thesis project, from the start to 27 Nov 2026

For an LLM assistant taking over this project. It describes what exists, what was done, what the numbers are and what is open. Read it fully before acting. Where a detail is not here, read the linked note on the `docs` branch or the code; do not guess.

---

## 1. Who and what

- **Thesis:** an LLM agent that does test-driven development (TDD) at class level, evaluated on the ClassEval benchmark (100 Python classes). Prior work he builds on: TGen (Mathews & Nagappan, "Test-Driven Development for Code Generation", arXiv:2402.13521).
- **Deadline:** he wants to submit before 23 Dec 2026 (official submission Mon 4 Jan 2027).
- **Repo:** `github.com/ioni-abc/tdd-agent` (local on his Mac: `~/Desktop/THESIS/tdd-agent`). Python 3.12, `uv`. Model: `claude-haiku-5-5` (`src/tdd_agent/config.py`, `MODEL`), `MAX_TOKENS = 8000`.
- **Overview canvas:** Lucidspark board "yes" (https://lucid.app/lucidspark/58514b97-e483-41aa-b05b-9599dffa2071/edit). Its sections, top to bottom: "First inspection & First fix" (steps 1 to 4 below), "Experiments" (three agents and their results, with link boxes to the docs notes), "Investigation: Are there inconsistencies between BM's tests and BM's docstrings?" (the labeling flow and the label counts), and the "Pass rate per test label" table (section 9). "BM" on the canvas means the benchmark.

## 2. Working rules set (follow them)

- **Answers:** brief, headlines and bullets, no chatter. No vague labels ("the spec is silent", "reference solution"): name things as the code names them (`task["solution_code"]`, `methods_info[i]["test_class"]`, exact paths and line numbers). Only state a number where it is obvious what it counts.
- **Explaining code:** part by part, argument by argument; use a real example from the data when asked.
- **Be precise and consistent.** Do not swap a definition (e.g. which labels count as "stated") without saying so. Do not use analogies unless asked. Say what was checked and what was not.
- **He prefers to try things himself first.** Do not run anything that costs money (API calls) without asking. The workspace may have no API key; then give him the exact command.
- **Models:** only the cheap model (Haiku) from now on. Never mention the results of the expensive model in answers, tables or charts. Earlier result files are kept in the repo for reference only.
- **`tdd-mixed`:** leave it out of results and tables; it gives no new insight.
- **Git:** commits authored only by `Ioannis Nikolaou <ioxnikolaou@gmail.com>`, unsigned (`git -c commit.gpgsign=false commit`), no `Co-Authored-By` or `Claude-Session` lines. Notes and ADRs go only on the separate `docs` branch (never merged into `main`), with prefixes `docs(notes): …` / `docs(adr): …`. Ask before committing anything that was not requested.
- **Charts:** he draws them in Lucidspark. He often asks for a prompt for Lucid's AI (fonts given in pt, no dates, no code names on agent boxes unless he allows them, links as named boxes).

## 3. Repository map

### Branches and tags (remote)
- `main` (tip `6e9fee5`): agents, grader, scripts, runs up to the failure analysis.
- `test-method-vs-method-docstring`: the per-test labeling and re-score (section 8, 9). Not merged into `main`.
- `docs`: notes and ADRs only.
- Tags: `milestone/baseline-agent`, `milestone/tdd-v1`, `milestone/tdd-mixed-run`, `milestone/failure-analysis`, `milestone/fix-benchmark-tests` (snapshots of earlier stages).

### Data
- `data/ClassEval_data.json`: original, never edited.
- `data/test_fixes.json`: the fix log; `scripts/fix_benchmark.py` applies it to `data/ClassEval_data_fixed.json`, which every run uses.
- Fields used per task: `task["skeleton"]` (the class outline with docstrings; on the canvas "class outline"), `task["test"]` (the full test file, 2196 tests over 100 tasks), `task["solution_code"]`, `task["class_name"]`, `task["methods_info"][i]` with `method_name`, `method_description` (the method's signature and docstring), `test_class`, `test_code` (that method's test class), `solution_code`.
- 2088 tests belong to a method's test class; 108 are class-level tests (their class is in no `methods_info[i]["test_class"]`).

### Code (`src/tdd_agent/`)
- `config.py`, `dataset.py` (`load_tasks`, `clean_skeleton`, `methods_in_order`, `tests_for_method` = `method["test_code"]`), `llm.py` (`LLM.call`, `extract_code`), `prompts.py`, `runs.py`, `report.py`, `test_writing.py`, `grading/` (runner with a 5 s timeout, `parse_log`).
- `agents/baseline.py`, `agents/tdd.py` (TDD agent v1), `agents/tdd_own_tests.py`, `agents/tdd_mixed_tests.py`.

### Scripts
- `scripts/run_reference.py`, `fix_benchmark.py`, `generate.py <agent> [task ids]`, `grade_run.py <run>`, `grade_tests.py`, `analyse_failures.py`, `export_tasks.py`.
- On `test-method-vs-method-docstring`: `scripts/label_tests.py`, `scripts/rescore_stated.py`.

### Results
- `results/reference/`: reference and empty-skeleton runs.
- `results/experiments/<run>/`: `run.json`, `calls/`, `code/`, `steps/`, `grades/<task>.json` (`counts`, `class_passed`, `timed_out`, `log`), for `tdd-own` also `tests/`, `tests_on_solution/`, `analysis/`.
- `results/analysis/`: `benchmark_labels.csv` (current labels), `benchmark_labels_old_prompt.csv` (Haiku, earlier judge prompt), `benchmark_labels_claude-sonnet-5-5.csv` (reference only, do not use or report), `rescore_stated.csv`, `tasks_readable/ClassEval_<n>.md` (one readable file per task), `docstring_examples.json`.

### Docs (`docs` branch)
- `docs/README.md` indexes everything. Key notes: `project-timeline.md`, `reference-run.md`, `benchmark-fixes.md`, `baseline-results.md`, `tdd-agent.md`, `runs-on-fixed-benchmark.md`, `tdd-own-results.md`, `results-of-insception-run-for-inconsistencies.md`, `label-examples.md`, `cross-check-results-and-where-we-stand.md`.
- ADRs 001 to 015 in `docs/decisions/` (e.g. 005 fix the benchmark as logged data, 011 TDD v1 sees all of ClassEval's tests, 012 the TDD loop, 014 sampled decoding: the API no longer allows setting temperature, so every run is one sample).
- Known stale content: `project-timeline.md` step 9 and `results-of-insception-run-for-inconsistencies.md` still show the earlier labeling and two-judge re-score numbers (including `tdd-mixed`). The current numbers are in `cross-check-results-and-where-we-stand.md`. Update only if user asks.

## 4. How the project unfolded

### Step 1: reference run and benchmark fixes
- ClassEval's `task["solution_code"]` against `task["test"]`: 96/100 on the first run; a rerun gave 95/100. Broken: 17 (test depends on today's date), 48 (depends on the machine's hostname), 31 and 51 (exact float comparison), 58 (flaky: the solution can place two mines on one cell).
- Fixed as data (`data/test_fixes.json`): 17 date moved to 2124, 48 `socket.gethostbyaddr` mocked, 31 and 51 `assertAlmostEqual`, 58 the solution fixed. After fixes: 100/100, 2196/2196.
- Empty skeletons: 0/100 classes; 157 of 2124 tests pass by accident (empty methods return `None`, which some tests accept).
- Notes: `reference-run.md`, `benchmark-fixes.md`.

### Step 2: baseline agent (canvas: "#1 no-tests-agent")
- One LLM call per class: `CODER_SYSTEM` + "Implement this class:" + skeleton.
- First run 48/100; on the fixed benchmark **51/100**, 1990/2196 tests (90.6%). Run `baseline_2026-11-19T14-38-59`.
- Its 49 failing classes were never analysed one by one.

### Step 3: TDD agent v1 (canvas: "#2 bm-tests-agent")
- Per method in `methods_in_order`: add the method's `test_code` to the suite, run (red), if failing call `TDD_IMPLEMENT`, run again, up to 3 `TDD_FIX` calls. The skeleton is kept in every prompt as a fixed specification. The final code is the last reply.
- It sees the method tests it is graded on (about 95% of graded tests; never the 108 class-level ones). ADR 011.
- **97/100**, 2168/2196 (98.7%). Run `tdd_2026-11-19T14-38-58`.
- Its three failures (`runs-on-fixed-benchmark.md`): ClassEval_25 (benchmark: a tested method `set_cookies` is not in the skeleton), ClassEval_49 (benchmark: helper `matches_requirements` named in a docstring, signature and behaviour unstated), ClassEval_31 (agent: 8 of 13 replies hit the 8000-token limit, empty replies overwrote the class, 0/21).

### Step 4: TDD agent with its own tests (canvas: "#3 own-tests-agent")
- For each method it first writes 5 tests from the docstring (prompt "write tests"), then runs the same red/green loop on its own tests. It never sees `task["test"]`. Commit `554c921` rejects written tests that fail to load.
- Three evaluations (`tdd-own-results.md`): its code vs the benchmark's tests **43/100** (1954/2196, 89.0%); its code vs its own tests 100/100 (2050/2050); `task["solution_code"]` vs its own tests 59/100 (1917/2050, 93.5%; 17 classes fail exactly 1 test, 24 fail 2 or more).
- Run `tdd-own_2026-11-19T14-38-57`.

### Step 5: mixed agent
- Some given tests, the rest its own: 68/100. Not rerun after the fixes and dropped from results.

### Step 6: failure analysis of `tdd-own`
- `scripts/analyse_failures.py`: 242 failing tests in 57 classes; most were on the benchmark side (the docstring does not state what the test checks). This raised the doubt that ClassEval's docstrings and tests are not in harmony.

### Step 7: meeting with the professor (20 Nov)
- The professor's thought experiment: approach #1 gets specs and tests, approach #2 gets only specs and writes its own tests. If the tests are wrong, #1 will chase them; fix the tests and #2 may look better. Evaluate both against a third, correct set of tests.
- His "number one" point: the agent was given wrong tests and did whatever it took to pass them; a human developer would have stopped and said the tests are wrong.
- user's worry: "agents need supervision, wrong input gives wrong output" is obvious and not a thesis finding. Most effort went into the benchmark, not into knowledge about agents.
- Agreed: check the benchmark itself, independent of any agent run.

### Step 8: per-test labeling (branch `test-method-vs-method-docstring`)
- `scripts/label_tests.py`, one LLM call per test, per test only (not per method):
  1. split `task["test"]` into single test functions with `ast` (`list_tests`; each with its class's `setUp`);
  2. match each test's class to `methods_info[i]["test_class"]` to find its method (no match = `no_method_info`, no call);
  3. send the judge the method's `method_description`, its `solution_code` and the test's source;
  4. the judge replies `PREDICTION`, `LABEL`, `REASON`, `MISSING`; `parse_reply` keeps `LABEL`, `REASON`, `MISSING`.
- Labels: `stated` (the docstring supports what the test checks), `unstated` (the docstring does not say), `contradicts` (the docstring says something else; the test and `solution_code` agree with each other), `other_inconsistency` (e.g. the test is filed under one method but calls another; example ClassEval_1 `test_calculate_sphere_area_2` calls `calculate_circle_area`).
- Judge prompt `JUDGE_SYSTEM` was rewritten in commit `06939cd` (explicit steps: read the test's setup and inputs, predict from the docstring alone, then compare with the assertion and `solution_code`), because the earlier wording was ambiguous.
- **Current labels** (`benchmark_labels.csv`, Haiku, new prompt), of 2088 judged tests: `stated` 1572 (75.3%), `unstated` 414 (19.8%), `contradicts` 44 (2.1%), `other_inconsistency` 58 (2.8%); plus 108 `no_method_info`. The earlier prompt gave 1565 / 418 / 38 / 67; 91.7% of tests got the same label under both prompts.
- Examples with code: `label-examples.md` and the readable files in `results/analysis/tasks_readable/`.

### Step 9: cross-check (re-score per label)
- `scripts/rescore_stated.py` (one labeling, default runs baseline, tdd, tdd-own): parses each `grades/<task>.json` `log` line `test_x (temp_file.Class.test_x) ... ok|FAIL|ERROR` into a dict `(task_id, class, test) -> passed`, reads the labels into a dict with the same key, and sums passed/total per label. `tdd-own` has 5 extra keys (ClassEval_7, its own test class left in its code); they are not in the labels and are skipped.

| Label (tests) | no-tests-agent | bm-tests-agent | own-tests-agent |
| --- | --- | --- | --- |
| `stated` (1572) | 1527 (97.1%) | 1559 (99.2%) | 1523 (96.9%) |
| `unstated` (414) | 307 (74.2%) | 407 (98.3%) | 286 (69.1%) |
| `contradicts` (44) | 15 (34.1%) | 44 (100.0%) | 13 (29.5%) |
| `other_inconsistency` (58) | 55 (94.8%) | 58 (100.0%) | 54 (93.1%) |
| `no_method_info` (108) | 86 (79.6%) | 100 (92.6%) | 78 (72.2%) |
| Classes passing all tests, as graded | 51/100 | 97/100 | 43/100 |
| Classes passing all their `stated` tests | 86/99 | 98/99 | 84/99 |

(99: ClassEval_69 has no `stated` test.)

### Step 10: tried and removed (27 Nov)
- A "doubt check" (asking the agent whether its given tests fit the docstring) and a `tdd-doubt` agent were written and then removed at user's request (code reverted in `dcd17fb`, note removed in `fcb370e`). Do not reintroduce them unless he asks.

## 5. What the results support, and what not

- **Supported:** on tests the docstring backs, the three agents are within about 2 points. Most of the headline gap (54 classes) is in tests the docstring does not back; on `stated` tests it falls to 14. Given tests, the bm-tests-agent satisfies all 44 `contradicts` tests, i.e. it follows the tests over the docstring.
- **Not supported:** that writing its own tests helps (own-tests-agent is at or below the baseline); that the bm-tests-agent implements specs better (it sees the tests it is graded on); anything needing error bars (one sample per agent, 100 tasks, labels from one unchecked LLM judge, `contradicts` only 44 tests).

## 6. Where the thesis stands (the open problem)

- user's concern, which is the main thing to help with: most of the work went into ClassEval's defects, not into an experiment that produces knowledge about agents. Without the benchmark work the rest is not at semester-thesis level. There is no decisive experiment yet.
- The professor's test for the thesis: "How is what I'm reading relevant and interesting to the reader?"
- See `docs/notes/cross-check-results-and-where-we-stand.md`.


## 7. Open items (only on users's request)

- Decide the research question with the professor.
- Possible options raised earlier: fix the `contradicts` docstrings; rewrite the `unstated` docstrings; hand-check a sample of labels; several samples per task for error bars; the professor's "third, correct test set" evaluation.
- Investigate the baseline's 49 failing classes (never done).
- Update stale numbers in `project-timeline.md` step 9 and `results-of-insception-run-for-inconsistencies.md`.

## 8. Commands (from the project root, on `test-method-vs-method-docstring`)

```bash
uv run python scripts/generate.py baseline|tdd|tdd-own [ClassEval_0 ...]   # costs money
uv run python scripts/grade_run.py <run folder name>
uv run python scripts/label_tests.py --dry-run                              # free
uv run python scripts/label_tests.py                                        # about 2088 Haiku calls, cached
uv run python scripts/rescore_stated.py                                     # free
uv run python scripts/export_tasks.py                                       # free
```
