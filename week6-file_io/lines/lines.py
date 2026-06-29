# expects exactly one command-line argument, the name (or path) of a Python file => len(sys.arv) = 2 ✔
    # sys.arv[0] = program name | sys.argv[1] = python file ✔
# the program should instead exit via sys.exit: ✔
#     If the user does not specify exactly one command-line argument ✔
#     or if the specified file’s name does not end in .py ✔
#     or if the specified file does not exist ✔
# excluding comments and blank lines:
    # Assume that any line that starts with #, optionally preceded by whitespace, is a comment. ✔
    # (A docstring should not be considered a comment. ✔
    # Assume that any line that only contains whitespace is blank. ✔
# outputs the number of lines of code in that file ✔

import sys


def main():
    # check the command-line argument
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # Check for python format 
    if not filename.endswith(".py"):
        sys.exit("Not a python file")

    # Check for existance of the file
    try:
        # outputs the number of lines of code
        print(count_lines(filename))
    except FileNotFoundError:
        sys.exit("File does not exist.")


# counting the line of codes in file
def count_lines(filename):
    count = 0
    with open(filename) as file:
        for line in file:
            # Eliminate whitespaces from line
            line = line.strip()

            # Eliminate whitespace and comment
            if line != "" and not line.startswith("#"):
                count += 1
    
    return count


if __name__ == "__main__":
    main()