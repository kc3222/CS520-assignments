# Part 3 — Fault Detection Check

This directory contains buggy versions of the solutions to evaluate whether the test suite catches bugs.

## Problem 1: sum_gp (491_1)

### Bug Injected

**Bug Type:** Off-by-one error in geometric progression formula

**Bug Description:** The buggy version uses `r ** (n - 1)` instead of `r ** n` in the geometric progression formula. This is a realistic bug that commonly occurs when implementing geometric series formulas, as developers may confuse the number of terms with the exponent needed.

**Bug Location:** `solution_buggy.py` line 6
```python
# Correct: return a * (1 - r ** n) / (1 - r)
# Buggy:   return a * (1 - r ** (n - 1)) / (1 - r)
```

**Why it's realistic:**
- Off-by-one errors are among the most common programming mistakes
- Geometric progression formulas are prone to confusion between term count and exponent
- This bug would pass many basic tests but fail on edge cases and specific inputs

### Test Results

When running the test suite against `solution_buggy.py`:

```bash
cd 491_1
# Replace solution.py with solution_buggy.py temporarily
pytest tests.py -v
```

**Tests that caught the bug:**
- `test_sum_gp_1()` - Failed: Expected 31, got 15
- `test_sum_gp_2()` - Failed: Expected 341, got 85
- `test_sum_gp_3()` - Failed: Expected 728, got 242
- Most tests in the suite failed, as the bug affects the core calculation

**Tests that passed:**
- `test_sum_gp_n_zero()` - Passed (boundary case handled correctly)
- `test_sum_gp_n_negative()` - Passed (boundary case handled correctly)
- `test_sum_gp_r_one()` - Passed (special case handled correctly)

### Conclusion

The test suite successfully detected the bug. The comprehensive test cases covering various input combinations (different values of a, n, and r) exposed the off-by-one error in the geometric progression formula. The branch coverage for the `r != 1` path was critical in catching this bug, as it exercised the main calculation logic where the error occurred. The boundary tests (n <= 0, r == 1) correctly passed, indicating that the bug was isolated to the main formula implementation.

**Coverage ↔ Fault Detection Link:** The branch coverage for the `r != 1` path, combined with diverse test inputs, exposed the off-by-one error in the exponent calculation. Without comprehensive branch coverage and multiple test cases with different parameter combinations, this subtle bug might have gone undetected.

---

## Problem 2: num_position (944_1)

### Bug Injected

**Bug Type:** Off-by-one error in index return value

**Bug Description:** The buggy version returns `i + 1` instead of `i`, providing a 1-based index instead of the expected 0-based index. This is a realistic bug that commonly occurs due to confusion between 0-based and 1-based indexing conventions.

**Bug Location:** `solution_buggy.py` line 5
```python
# Correct: return i
# Buggy:   return i + 1
```

**Why it's realistic:**
- Indexing errors are extremely common in programming
- Confusion between 0-based and 1-based indexing is a frequent source of bugs
- This bug would cause all position values to be off by 1, which is easy to miss in manual testing

### Test Results

When running the test suite against `solution_buggy.py`:

```bash
cd 944_1
# Replace solution.py with solution_buggy.py temporarily
pytest tests.py -v
```

**Test Results:**
- **106 tests failed** - All tests that verify specific position values failed due to the off-by-one error
- **4 tests passed** - Edge cases that return -1 (no digit found) passed correctly

**Examples of tests that caught the bug:**
- `test_num_position_1()` - Failed: Expected 10, got 11
- `test_num_position_2()` - Failed: Expected 17, got 18
- `test_num_position_3()` - Failed: Expected 9, got 10
- `test_num_position_4()` - Failed: Expected 1, got 2
- `test_num_position_only_digits()` - Failed: Expected 0, got 1
- `test_num_position_single_digit()` - Failed: Expected 0, got 1
- `test_num_position_digit_at_end()` - Failed: Expected 6, got 7
- All 102 numbered test cases (test_num_position_1 through test_num_position_102) failed
- All coverage improvement tests that check specific positions failed

**Tests that passed:**
- `test_num_position_empty_string()` - Passed (returns -1 correctly)
- `test_num_position_no_digits()` - Passed (returns -1 correctly)
- `test_num_position_no_digits_with_spaces()` - Passed (returns -1 correctly)
- `test_num_position_no_digits_special_chars()` - Passed (returns -1 correctly)

### Conclusion

The test suite successfully detected the bug with **106 out of 110 tests failing**. The comprehensive test cases with known expected positions exposed the off-by-one error in the index return value. The branch coverage for the "digit found" path was critical in catching this bug, as it exercised the return statement where the error occurred. The edge case tests (empty string, no digits) correctly passed, indicating that the bug was isolated to the index calculation when a digit is found.

**Coverage ↔ Fault Detection Link:** The branch coverage for the "digit found" path, combined with tests that verify exact position values, exposed the off-by-one error in the index return. Without branch coverage of the return path and tests with specific expected position values, this indexing bug might have gone undetected, especially if only correctness (digit found vs. not found) was tested rather than exact position values. The fact that 96.4% of tests failed demonstrates the effectiveness of comprehensive test coverage in detecting this type of bug.

---

## Running the Fault Detection Check

To verify the bugs are caught:

1. **For Problem 1 (491_1):**
   ```bash
   cd 491_1
   cp solution.py solution_correct.py  # Backup correct solution
   cp solution_buggy.py solution.py    # Use buggy version
   pytest tests.py -v                  # Run tests (should fail)
   cp solution_correct.py solution.py  # Restore correct solution
   ```

2. **For Problem 2 (944_1):**
   ```bash
   cd 944_1
   cp solution.py solution_correct.py  # Backup correct solution
   cp solution_buggy.py solution.py   # Use buggy version
   pytest tests.py -v                  # Run tests (should fail)
   cp solution_correct.py solution.py  # Restore correct solution
   ```

## Summary

Both buggy versions were successfully detected by the test suites. The comprehensive coverage, including:
- Multiple test cases with diverse inputs
- Branch coverage of all code paths
- Edge case testing (boundary conditions, empty inputs)
- Tests that verify exact expected values (not just correctness)

...ensured that realistic bugs (off-by-one errors) were caught. This demonstrates that high code coverage, when combined with well-designed test cases that verify specific expected behaviors, is effective at fault detection.

