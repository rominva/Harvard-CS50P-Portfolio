# prompts the user for their date of birth in "YYYY-MM-DD" format ✔
# and then sings/prints how old they are in minutes ✔
    # rounded to the nearest integer ✖
    # using English words instead of numerals ✔
    # just like the song from Rent, without any and between words ✔
# assume that the user was born at midnight (i.e., 00:00:00) on that date ✔
    # And assume that the current time is also midnight ✔
    # In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date ✔
# You’re welcome to import other (built-in) libraries, or any that are specified in the below hints ✔
# Exit via sys.exi if the user does not input a date in YYYY-MM-DD format => "Invalid date" ✔
# Ensure that your program will not raise any exceptions ✔
# ✅ 1970-01-01

from datetime import date, datetime
import inflect
import sys

p = inflect.engine()

def main():
    birth = input("Date of Birth: ")

    try:
        birth_date = extract_date(birth)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()

    if birth_date > today:
        sys.exit("Invalid date")

    delta_time = date_difference(birth_date, today)
    minutes =  calculate_total_minutes(delta_time)
    
    print(sing(minutes))


def extract_date(date_str):
    birth_date = datetime.strptime(date_str, "%Y-%m-%d").date() # to turn into date format
    return birth_date


def date_difference(day1, day2):
    difference = day2 - day1
    return difference # in timedelta format


def calculate_total_minutes(date_difference):
    total_days = date_difference.days # .days => timedelta attributes that eliminate the clock
    total_minutes = total_days * 24 * 60
    return total_minutes


def sing(count):
    return f"{p.number_to_words(count)} {p.plural_noun('minute', count)}".capitalize().replace(" and ", " ")


if __name__ == "__main__":
    main()