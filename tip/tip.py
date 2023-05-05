def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}\n")


def dollars_to_float(d):

    d = d.split('$')[1]
    return float(d)


def percent_to_float(p):
    p = float(p[:-1]) / 100
    return p


if __name__ == '__main__':
    main()