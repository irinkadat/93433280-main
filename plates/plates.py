def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(txt):
    
    while True:
        if len(txt) < 2 or len(txt) > 6:
            return False

        for l in txt[:2]:
            if not l.isalpha():
                return False

        for n in txt:
            if n.isdigit():
                index = txt.index(n)
                if not txt[index:].isdigit():
                    return False

        i = 0
        while i < len(txt):
            if txt[i].isdigit() == True:
                if txt[i] == "0":
                    return False
                break
            i += 1

        for i in txt:
            if i.isdigit():
                if i == '0':
                    return False
                return True



        for s in txt:
            if s in [".", ",", "!", "?", " ", "\"", "\'"]:
                return False

        return True


main()