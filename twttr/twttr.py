def main():
    text = input("Enter some text: ")
    without_vowels = remove_vowels(text)
    print(f"Text without vowels: {without_vowels}")

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join([char for char in text if char not in vowels])


if __name__=="__main__":
    main()