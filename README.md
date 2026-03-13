Focus: Python code review, refactoring, and unit testing examples prepared for AI code evaluation tasks.
# adedayo-g2i-samples

Small, focused samples prepared for applications to roles like **AI Software Engineer (Python)** (code review / RLHF-style tasks).

## Contents
- `after.py` — Final code for the "find duplicates" example (O(n) solution with deterministic output).
- `tests.py` — pytest tests for `after.py`.
- `refactor/` — contains an example before/after refactor using `collections.Counter`:
  - `refactor/before_refactor.py`
  - `refactor/after_refactor.py`
  - `refactor/tests_refactor.py`

## How to run tests
1. Ensure Python 3.8+ is installed.
2. Install `pytest` if not present:
   ```bash
   pip install pytest
