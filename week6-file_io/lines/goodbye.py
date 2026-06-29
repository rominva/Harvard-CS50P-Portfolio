import random

def main():
    level = get_level()
    score = 0

    # Randomly generates 10 math problems formatted as (X + Y = )
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        true_answer = x + y

        # allowing the user up to three tries in total
        for _ in range(3):
            try:
                # Prompts the user to solve
                user_answer = int(input(f"{i+1}) {x} + {y} = "))
                
                if user_answer == true_answer:
                    score += 1
                    break
                else:
                    raise ValueError   
            except ValueError:
                print("EEE")
        else:
            # If not answered correctly after three tries, output the correct answer.
            print(f"{x} + {y} = {true_answer}")
    
    print(f"Score: {score}")


# Prompts the user for a level, 𝑛 = "1", "2" or "3"
def get_level():
    while True:
        n = input("Level: ").strip()
        if n in ["1", "2", "3"]:
            return n


# create a single randomly generated non-negative integer with level
def generate_integer(level):
    if level not in ["1", "2", "3"]:
        raise ValueError
    
    if level == "1":
        num = random.randint(0,9)
    elif level == "2":
        num = random.randint(10, 99)
    else:
        num = random.randint(100, 999)

    return num


if __name__ == "__main__":
    main()
