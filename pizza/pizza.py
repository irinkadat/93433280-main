from tabulate import tabulate
import csv, sys

def main():
    file = check_args()

    if not file.endswith('.csv'):
        sys.exit('Not a CSV file')
    else:
        print(tabulate_menu(file))


def check_args():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        return sys.argv[1]

def tabulate_menu(file):
    try:
        with open(file, 'r') as f:
            reader = csv.reader(f)
            header = next(reader) #next() function to extract the first row of the CSV file, which is assumed to be the header row.
            menu = []
            for line in reader:
                menu.append(line)

    except FileNotFoundError:
        sys.exit('file not found :(')

    return tabulate(menu, header, tablefmt="grid")

if __name__=='__main__':
    main()