# implement a function called count that expects a line of text as input as a str ✔
# and returns, as an int, the number of times that “um” appears in that text  ✔
    # case-insensitively  ✔
    # word unto itself, not as a substring of some other word ✔

import re


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()