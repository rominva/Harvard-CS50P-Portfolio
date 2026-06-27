# Fuel Gauge

def main():
    while True:
        # Prompts user for fraction as X/Y
        fraction = input("fraction: ")
        try:
            percentage = convert(fraction)
            print(gauge(percentage))
            break

        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    # Extract x, y as an integer
    x, y = map(int, fraction.split("/"))
    percentage = round(x / y * 100)

    # Tank overload
    if x > y:
        raise ValueError

    # To avoid negative inputs
    if x < 0 or y < 0:
        raise ValueError

    return percentage


def gauge(percentage):
    # Output
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
