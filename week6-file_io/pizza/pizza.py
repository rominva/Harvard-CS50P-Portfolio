# expects exactly one command-line argument, the name (or path) of a CSV file ✔
# outputs a table formatted as ASCII art using tabulate, a package on PyPI ✔
    # Format the table using the library’s grid format ✔

# the program should instead exit via sys.exit. ✔
    # If the user does not specify exactly one command-line argument ✔
        # "Too few command-line arguments"  ✔
        # "Too many command-line arguments"  ✔
    # or if the specified file’s name does not end in .csv ✔
        # "Not a CSV file" ✔
    # or if the specified file does not exist ✔

from tabulate import tabulate
import csv
import sys


def main():
    # Check for command-line argument => sys.argv[0]="pizza.py" | sys.argv[1]=filename
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # Check for csv format
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    # check the existance of the file
    try:
        menu_list = readfile(filename)
    except FileNotFoundError:
        sys.exit("File does not exist")


    # outputs a table formatted as ASCII art using "tabulate" in "grid" format
    print(tabulate(menu_list, headers="keys", tablefmt="grid"))


def readfile(filename):
    menu = []
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu.append(row)

    # list or another iterable of dicts (keys as columns)
    return menu


if __name__ == "__main__":
    main()
