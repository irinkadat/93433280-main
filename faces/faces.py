def main():
    input_txt = input('')
    print(convert(input_txt),end='')
def convert(input_txt):
    res = input_txt.replace(":(", "🙁").replace(":)", "🙂")
    return res

if __name__ == "__main__":
    main()
