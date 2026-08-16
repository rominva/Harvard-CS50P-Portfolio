# implement a program that prompts the user for an email address via input
# then prints Valid or Invalid
    # You may not use re. 
    # And do not validate whether the email address’s domain name actually exists.

import validators

def main():
    user_input = input("Email: ")
    if validate_mail(user_input):
        print("Valid")
    else:
        print("Invalid")


def validate_mail(s):
    return bool(validators.email(s))


if __name__ == "__main__":
    main()