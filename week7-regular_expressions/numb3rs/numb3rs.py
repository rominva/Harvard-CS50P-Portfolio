# validate that expects an IPv4 address as input as a str
# #.#.#.# But each # should be a number between 0 and 255
# then returns True or False, respectively, if that input is a valid IPv4 address or not.
# modify main and/or implement other functions as you see fit
# but you may not import any other libraries
# You’re welcome, but not required, to use re and/or sys


import re


def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))


def validate(ip):
    #.#.#.# (0-255)
    digits = r"(0|[1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
    pattern = rf"{digits}\.{digits}\.{digits}\.{digits}" 
    return bool(re.fullmatch(pattern, ip))


if __name__ == "__main__":
    main()