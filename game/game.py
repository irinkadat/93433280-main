import random

def main():
    while True:
        try:
            level = int(input('Level: '))
            if level <= 0:
                print('Please enter a positive integer.')
            else:
                break
        except ValueError:
            print('Please enter a valid integer.')

    while True:
        try:
            guess = int(input('Guess: '))
            if guess <= 0:
                print('Please enter a positive integer.')
            elif guess > level:
                print('Please enter a guess smaller than or equal to the level.')
            else:
                break
        except ValueError:
            print('Please enter a valid integer.')

    print(guess_game(level, guess))

def guess_game(level, guess):

    while True:
        num = random.randint(1, level)
        if guess > num:
            print('Too large!')
        elif guess < num:
            print('Too small!')
        else:
            print('Just right!')
            break


if __name__ == '__main__':
    main()
