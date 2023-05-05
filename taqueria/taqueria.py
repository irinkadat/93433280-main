def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    order(menu)


def order(menu):

    total = 0
    while True:
        try:
            meal = input("Enter meal: ").title().strip()
            total += menu[meal]
        except KeyError:
            print("Invalid meal entered, please try again.")
        except EOFError:
            print("Your order has been received!")
            break

        print(f"Total: ${total:.2f}")


if __name__=="__main__":
    main()
