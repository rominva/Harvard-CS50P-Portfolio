# Bitcoin Price Index

A Python program that retrieves the current Bitcoin price from the CoinCap API and calculates the cost of a specified number of Bitcoins in USD.

## Problem Description

This project was completed as part of **Harvard CS50P (CS50's Introduction to Programming with Python)**.

The program:

- Accepts the number of Bitcoins to purchase as a command-line argument.
- Retrieves the current Bitcoin price from the CoinCap API.
- Calculates the total cost in USD.
- Formats the result using thousands separators and four decimal places.
- Handles invalid user input and network-related errors.

## Concepts Practiced

- Command-line arguments (`sys.argv`)
- Exception handling (`try` / `except`)
- Working with APIs
- JSON parsing
- HTTP requests with `requests`
- Numeric formatting
- Data validation

## Requirements

Install the required package:

```bash
pip install requests
```

You will also need a CoinCap API key.


Before running the program, replace:

```python
YourApiKey = "YOUR_API_KEY_HERE"
```

with your own CoinCap API key.


## Usage

```bash
python bitcoin.py 2
```

Example output:

```text
$129,192.7000
```

## Error Handling

The program handles several error conditions:

- Missing command-line argument
- Non-numeric input
- API connection failures
- Missing data in the API response

## Project Structure

```text
bitcoin/
├── bitcoin.py
└── README.md
```

## Technologies Used

- Python 3
- Requests
- CoinCap API
- JSON


## License

This project is provided for educational purposes as part of the CS50P course.