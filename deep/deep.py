def main():
    res =  input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()
    print(check(res))

def check(res):
    answers = ["42", "forty-two", "forty two"]

    if res.strip() in answers:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    main()