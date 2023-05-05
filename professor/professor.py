import random

def main():
    level = get_level()
    score = 0
    for i in range(10):
        x, y = generate_integer(level)
        problem = f"{x} + {y} = "
        answer = None
        attempt = 0
        while answer != x + y:
            attempt += 1
            if attempt == 3:
                print(problem + str(x + y))
                break
            answer = input(problem)
            try:
                answer = int(answer)
            except ValueError:
                answer = None
            if answer != x + y:
                print("EEE")
            else:
                score += 1
    print(score)

def get_level():
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return int(level)

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError("Invalid level")
    return x, y

if __name__ == "__main__":
    main()

