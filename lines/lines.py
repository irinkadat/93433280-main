import sys

def main():
    file = check_args()

    if not file.endswith('.py'):
        sys.exit('Not a Python file')
    else:
        print(count_lines(file))


def check_args():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        return sys.argv[1]

def count_lines(file):
    try:
        with open(file, 'r') as f:
            count = 0
            for line in f:
                line = line.lstrip()
                if len(line) == 0 or line.startswith('#'):
                    count += 0
                else:
                    count += 1

    except FileNotFoundError:
        sys.exit('file not found :(')

    return f'line count in file is : {count}'

if __name__=='__main__':
    main()