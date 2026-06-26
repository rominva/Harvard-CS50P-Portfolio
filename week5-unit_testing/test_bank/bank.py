# prompts the user for a greeting
# If greeting starts with “hello” => output $0
# If greeting starts with an “h” (but not “hello”) => output $20
# Otherwise => output $100
# Ignore any leading whitespace in the user’s greeting
# treat the user’s greeting case-insensitively

def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    greeting = greeting.lower().strip()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
