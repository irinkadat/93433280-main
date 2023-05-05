def main():
    get_grocery_items()

def get_grocery_items():
    grocery_items = []
    while True:
        try:
            item = input("").upper()
            grocery_items.append(item)

        except EOFError:
            break

    grocery_items = sorted(grocery_items)

    item_counts = {}
    for item in grocery_items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1

    for item, count in item_counts.items():
        print(f"{count} {item}")

if __name__=="__main__":
    main()

