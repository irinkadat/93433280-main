def coke_machine():
    print('Amount Due: 50')

    total = 0
    while total < 50:
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            total += coin
            print(f"Amount Due: {50 - total}")
        else:
            print(f"Amount Due: {50 - total}")

    if total > 50:
        change = total - 50
        print(f"Change Owed: {change}")
    else:
        print("Change Owed: 0")


coke_machine()