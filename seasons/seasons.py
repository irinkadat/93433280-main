from datetime import datetime, date
import inflect , sys

def main():
    birth = input("Date of Birth: ")
    try:
        birth_date = datetime.strptime(birth, "%Y-%m-%d").date()
    except ValueError:
        sys.exit('Invalid date format')

    age_in_minutes = calculate_minutes(birth_date)
    print(age_in_minutes)

def calculate_minutes(birth_date):
    birth_date = datetime.strptime(str(birth_date), "%Y-%m-%d").date()
    current_date = date.today()

    num_days = (current_date - birth_date).days

    minutes = num_days * 24 * 60

    p = inflect.engine()
    p.defnoun('minute', 'minutes')

    minutes_str = p.number_to_words(minutes, andword='', zero='')
    minutes_str = minutes_str[0].upper() + minutes_str[1:]

    return minutes_str + " minutes"



if __name__ == "__main__":
    main()

