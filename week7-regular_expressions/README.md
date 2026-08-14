# CS50P — Problem Set 7: Regular Expressions

This repository contains my solutions to **Problem Set 7** of [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/), focused on **Regular Expressions (Regex)** and input validation.

## 📚 About This Problem Set

Problem Set 7 introduces practical uses of regular expressions for recognizing patterns, validating input, extracting information, and transforming strings.

Through these five problems, I practiced using Python's `re` module alongside other validation techniques and testing with `pytest`.

## 🧩 Problems

### 1. NUMB3RS

**File:** `numb3rs/`

Validates whether a given string represents a valid IPv4 address.

This problem focuses on:

* Regular expression patterns
* Capturing groups
* Input validation
* Numeric range validation
* Testing edge cases with `pytest`
* Writing thorough unit tests

Special attention is given to IPv4 octets, which must contain values from `0` to `255`, as well as invalid formats such as leading zeros.

---

### 2. Watch on YouTube

**File:** `watch/`

Extracts a YouTube video ID from a URL and converts it into the corresponding YouTube embed URL.

This problem focuses on:

* Regular expressions
* Capturing groups
* Optional URL components
* `re.search()`
* Extracting information from structured strings

---

### 3. Working 9 to 5

**File:** `working/`

Converts time expressions from 12-hour format into 24-hour format.

For example:

```text
9 AM to 5 PM
```

becomes:

```text
09:00 to 17:00
```

This problem focuses on:

* Regular expressions
* Capturing groups
* Optional components
* String formatting
* Converting extracted data into a different representation

---

### 4. Regular, um, Expressions

**File:** `um/`

Counts occurrences of the word `um` in a sentence, regardless of capitalization or whether it appears between other words.

This problem focuses on:

* Word boundaries
* Case-insensitive matching
* `re.findall()`
* Quantifiers
* Designing patterns that distinguish a complete word from part of another word

---

### 5. Response Validation

**File:** `response/`

Validates whether an email address is syntactically valid using a validation library rather than regular expressions.

This problem focuses on:

* Input validation
* Third-party Python libraries
* Understanding the difference between syntactic validation and checking whether a domain actually exists
* Handling invalid user input

---

## 🛠️ Concepts Practiced

Throughout this problem set, I worked with:

* Regular Expressions (Regex)
* Python's `re` module
* `re.search()`
* `re.findall()`
* Capturing groups
* Character classes
* Quantifiers
* Anchors
* Word boundaries
* Case-insensitive matching
* Raw strings
* Input validation
* Edge-case testing
* `pytest`
* Third-party validation libraries

## 🧪 Testing

For problems that include tests, I used `pytest` to verify the behavior of my implementations and to check both valid and invalid inputs.

Example:

```bash
pytest test_numb3rs.py
```

Testing was particularly important for identifying edge cases that a simple implementation might overlook.

## 🎯 What I Learned

This problem set helped me move from understanding regular expressions as a collection of symbols to using them as a practical tool for **pattern recognition and validation**.

In particular, I practiced breaking a problem into:

1. Identifying the structure of the input.
2. Translating that structure into a regular expression.
3. Extracting the relevant information using capture groups.
4. Validating edge cases.
5. Testing the implementation against both expected and unexpected input.

## 📁 Repository Structure

```text
pset7/
│
├── numb3rs/
│   ├── numb3rs.py
│   └── test_numb3rs.py
│
├── watch/
│   └── watch.py
│
├── working/
│   └── working.py
│
├── um/
│   └── um.py
│
├── response/
│   └── response.py
│
└── README.md
```

## 🎓 Course

**CS50's Introduction to Programming with Python (CS50P)**
Harvard University — David J. Malan

* Course: https://cs50.harvard.edu/python/
* Week 7 — Regular Expressions: https://cs50.harvard.edu/python/weeks/7/
* Problem Set 7: https://cs50.harvard.edu/python/psets/7/

---

*Part of my journey through Harvard's CS50P — practicing Python, problem solving, testing, and writing cleaner code.*
