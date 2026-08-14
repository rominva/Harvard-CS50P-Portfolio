# implement a function called parse that expects a str of HTML as input like: ✔
    # <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# extracts any YouTube URL that’s the value of a src attribute of an iframe element therein ✔
# Expect that any such URL will be in one of the formats below: ✔
    # http://youtube.com/embed/xvFZjo5PgG0
    # https://youtube.com/embed/xvFZjo5PgG0
    # https://www.youtube.com/embed/xvFZjo5PgG0

#  and returns its shorter, shareable youtu.be equivalent as a str like: ✔
    # https://youtu.be/xvFZjo5PgG0

# Assume that the value of src will be surrounded by double quotes. ✔
# And assume that the input will contain no more than one such URL. ✔
# If the input does not contain any such URL at all, return "None" ✔

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/(.+?)"'
    if match := re.search(pattern, s):
        id = match.group(1)
    else:
        return None

    return f"https://youtu.be/{id}"


if __name__ == "__main__":
    main()