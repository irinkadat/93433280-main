def main():
    fuel_gauge()

def fuel_gauge():
    while True:
        fraction = input("enter fraction: ").strip()
        try:
            x, y = map(int, fraction.split('/'))
            percent = x / y * 100

        except ValueError:
            print("Invalid fraction format!")
            continue
        except ZeroDivisionError:
            print("Zero devision error!")
            continue


        if 99 <=percent <= 100:
            print("F")
        elif percent > 100:
            continue
        elif percent <= 1:
            print("E")
        else:
            print(f"{round(percent)}%")

        break

if __name__ == "__main__":
    main()
