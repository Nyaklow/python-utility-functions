# Python Utility Functions

A set of Python utility modules covering date handling, time validation, Roman numerals, and palindrome detection — each with a full unit test suite.

## Modules

### `dateutil.py`
Formats a date given day, month, and year into a human-readable string (e.g. `"15 April 2025"`). Validates leap years and month-specific day limits.

### `timeutil.py`
Validates time strings in 12-hour `h:mm a.m./p.m.` format, checking hours, minutes, and suffix correctness.

### `romanutil.py`
Converts Roman numeral strings (e.g. `"XIV"`) to their integer equivalents, handling subtractive notation correctly.

### `palindrome.py`
Checks whether a given string is a palindrome by comparing characters from both ends toward the centre.

## Unit Tests

| Test file | Covers |
|---|---|
| `testdateutil.py` | `dateutil.format_date` |
| `testtimeutil.py` | `timeutil.validate` |
| `testromanutil.py` | `romanutil.from_roman` |
| `testpalindrome.py` | `palindrome.is_palindrome` |

```bash
python -m pytest
```

## Author
Nyakallo Nyokong — University of Cape Town, BSc Business Science (Data Science & Statistics)
