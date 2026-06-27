# prompts the user for a vanity plate ✔
# output Valid if meets all of the requirements ✔
# or Invalid if it does not ✔
# Assume that any letters in the user’s input will be uppercase ✔
# requirements:
# All vanity plates must start with at least two letters.” ✔
# vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.” ✔
# Numbers cannot be used in the middle of a plate; they must come at the end. ✔
# (For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.)
# The first number used cannot be a ‘0’. ✔
# No periods, spaces, or punctuation marks are allowed. ✔

def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # check the existance
    if not s:
        return False

    # No periods, spaces, or punctuation marks are allowed
    if not s.isalnum():
        return False

    # vanity plates may contain a maximum of 6 chars and a minimum of 2 chars
    if not 2 <= len(s) <= 6:
        return False

    # All vanity plates must start with at least two letters
    if not s[0:2].isalpha():
        return False

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # The first number used cannot be a ‘0’
    for i in range(len(s)):
        if s[i].isdigit():
            # First digit
            if s[i] == "0":
                return False
            
            # After the first digit till the end
            for ch in s[i:]:
                if ch.isalpha():
                    return False

            return True

    return True


if __name__ == "__main__":
    main()
