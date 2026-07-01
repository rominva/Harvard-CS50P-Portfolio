# Expects two command-line arguments => len(sys.argv = 3) ✔
# sys.argv[1] => name of an existing CSV file to read as input, ✔
    # whose columns are assumed to be, in order, "name" and "house"
# sys.argv[2] => name of a new CSV to write as output, ✔
    # whose columns should be, in order, "first", "last", and "house" ✔

# Converts that input to that output, ✔
    # splitting each name into a "first name" and "last name". ✔
    # Assume that each student will have both a first name and last name. ✔

# the program should exit via "sys.exit" with an error message. ✔
    # If the user does not provide exactly two command-line arguments ✔
        # "Too few command-line arguments" ✔
        # "Too many command-line arguments" ✔
    # or if the first cannot be read ✔
        # "Could not read {filename}" ✔


# right example: python scourgify.py before.csv after.csv

import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]

    try:
        convert(inputfile, outputfile)
    except FileNotFoundError:
        sys.exit(f"Could not read the file")


def convert(inputfile, outputfile):
    with open(inputfile, "r") as infile, open(outputfile, "w", newline="") as outfile:
        reader = csv.DictReader(infile)    # "name" and "house"
        
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])   # "first", "last", and "house"
        writer.writeheader()
        
        for row in reader:
            last, first = row["name"].split(", ")
            house = row["house"]
            
            writer.writerow({"first": first, "last": last, "house": house})


if __name__ == "__main__":
    main()