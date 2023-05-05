import re

def main():
    count(input("enter s: "))

def count(s):
    pattern = r'\bum\b'
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)

if __name__== "__main__":
    main()