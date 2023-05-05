import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)"
    match = re.search(regex, s)
    if not match:
        raise ValueError("Invalid input format")

    start_hour, start_min, start_ampm, end_hour, end_min, end_ampm = match.groups()
    start_hour, end_hour = int(start_hour), int(end_hour)
    if start_hour == 12:
        start_hour = 0
    if end_hour == 12:
        end_hour = 0

    if start_ampm == "PM":
        start_hour += 12
    if end_ampm == "PM":
        end_hour += 12
    if not (0 <= start_hour < 24 and 0 <= end_hour < 24 and 0 <= int(start_min or 0) < 60 and 0 <= int(end_min or 0) < 60):
        raise ValueError("Invalid time")
    return f"{start_hour:02}:{start_min or '00'} to {end_hour:02}:{end_min or '00'}"


if __name__ == "__main__":
    main()

