import emoji

def main():
    print(emojize())


def emojize():
    text = input("enter text:")
    return emoji.emojize(text, language='alias')

main()