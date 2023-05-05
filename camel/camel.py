def main():
    var = input("Enter a variable name in camelCase: ")
    camelToSnake(var)

def camelToSnake(var):
    if var.islower() or var.isupper():
        raise ValueError("Variable name should be in camelCase format!")

    res = ""
    for i in var:
        if i.isupper():
            res += "_" + i.lower()
        else:
            res += i
    print(res)

main()
