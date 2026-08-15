# implement a function called convert that expects a str in any of the 12-hour formats below ✔
    # 9:00 AM to 5:00 PM
    # 9 AM to 5 PM
    # 9:00 AM to 5 PM
    # 9 AM to 5:00 PM
# Expect that AM and PM will be capitalized (with no periods therein) ✔
# and that there will be a space before each. ✔

#  and returns the corresponding str in 24-hour format (i.e., 09:00 to 17:00) ✔

# Raise a ValueError instead ✔
    # if the input to convert is not in either of those formats ✔
    # or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.) ✔

# But do not assume that someone’s hours will start ante meridiem and end post meridiem ✔
    # someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM). ✔

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    start_time = r"(?P<s_hour>[1-9]|1[0-2])(?::(?P<s_minute>00|0[1-9]|[1-5][0-9]))?"
    end_time = r"(?P<e_hour>[1-9]|1[0-2])(?::(?P<e_minute>00|0[1-9]|[1-5][0-9]))?"

    pattern = rf"{start_time} (?P<s_period>AM|PM) to {end_time} (?P<e_period>AM|PM)"

    matches = re.fullmatch(pattern, s)
    if not matches:
        raise ValueError 

    # Extract time from capturing groups
    # Start time:
    s_hour = matches.group("s_hour")

    if matches.group("s_minute"):
        s_minute = matches.group("s_minute")
    else:
        s_minute = "00"

    s_period = matches.group("s_period")

    # End time:
    e_hour = matches.group("e_hour")

    if matches.group("e_minute"):
        e_minute = matches.group("e_minute")
    else:
        e_minute = "00"

    e_period = matches.group("e_period")


    # Hour Conversion to 24 format
    s_hour = convert_24format(int(s_hour), s_period)
    e_hour = convert_24format(int(e_hour), e_period)


    return f"{s_hour:02}:{s_minute} to {e_hour:02}:{e_minute}"


def convert_24format(hour: int, period: str):
    if period == "PM":
        # 12 PM --> 12
        if hour != 12:
            hour += 12
    else:
        # 12 AM --> 0 
        if hour == 12:
            hour = 0

    return hour


if __name__ == "__main__":
    main()