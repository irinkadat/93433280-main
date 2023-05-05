def main():
    expression = input("Enter expression: ")
    x, y, z = expression.split(" ")
    print(calculate(float(x), y ,float(z)))

def calculate(x,y,z):
    if  y == "+":
        return x + z
    elif y == "-":
        return  x -z
    elif y == "/":
        if z == 0:
            return ZeroDivisionError
        return x / z

    elif y == "*":
        return x * z

if __name__=="__main__":
    main()