import sys, csv

def main():
    check_arg_validity()
    scourgify()


def check_arg_validity():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


def scourgify():
    try:
        with open(sys.argv[1], "r") as input_file, open(sys.argv[2], "w") as output_file:

            column_data = csv.DictReader(input_file, delimiter=",")
            column_writer = csv.DictWriter(output_file, ["first", "last", "house"])

            column_writer.writeheader()

            for row in column_data:
                last, first = row["name"].split(",")
                column_writer.writerow({
                    "first": first.strip(),
                    "last": last,
                    "house": row["house"]
                })

    except FileNotFoundError:
        sys.exit("Could not read file")


if __name__ == "__main__":
    main()
