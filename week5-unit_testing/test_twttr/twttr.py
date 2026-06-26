# implement a program that prompts the user for a str of text
# outputs that same text but without vowels (A, E, I, O, and U)
# whether inputted in uppercase or lowercase

def main():
    text = input("Input: ")
    print("Output:", shorten(text))


def shorten(word):
    vowels = "AEIOUaeiou"
    result = ""
    for l in word:
        if l not in vowels:
            result += l

    return result


if __name__ == "__main__":
    main()
