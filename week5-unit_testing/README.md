# CS50P – Problem Set 5: Unit Testing with Pytest

This repository contains my solutions for **Problem Set 5** of **CS50's Introduction to Programming with Python**.

The focus of this problem set is writing automated tests using **pytest** by testing previously implemented programs rather than writing new applications. :contentReference[oaicite:0]{index=0}

## Topics Covered

- Writing unit tests with `pytest`
- Organizing test cases into separate test functions
- Testing normal, edge, and invalid inputs
- Using `assert` statements
- Testing exceptions with `pytest.raises`
- Improving code reliability through automated testing

## Exercises

### Testing my twttr
- Tested removal of vowels from strings.
- Covered words with and without vowels.
- Verified behavior for numbers, punctuation, and empty strings.

### Back to the Bank
- Tested greeting classification logic.
- Verified greetings beginning with "hello", greetings starting with "h", and all other inputs.
- Included different capitalizations and punctuation.

### Re-requesting a Vanity Plate
- Tested license plate validation rules, including:
  - Minimum and maximum length
  - Starting with at least two letters
  - Alphanumeric characters only
  - Numbers appearing only at the end
  - First number not being `0`

### Refueling
- Tested both conversion and gauge functionality.
- Verified valid percentages.
- Tested invalid fractions and expected exceptions using `pytest.raises`.
- Covered boundary values such as empty and full fuel tanks.

## Requirements

- Python 3.12+ (or compatible)
- pytest

Install pytest with:

```bash
pip install pytest
```

## Running the Tests

Run all tests with:

```bash
pytest
```

Or run a specific test file:

```bash
pytest test_plates.py
```

## Course

These exercises are part of **CS50's Introduction to Programming with Python** by Harvard University.

https://cs50.harvard.edu/python/