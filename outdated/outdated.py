MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def get_month_numeral(month_name):
    for i in range(len(MONTHS)):
        if month_name == MONTHS[i]:
            return i + 1

def date_validation(month, day):
    return (int(month) > 0 and int(month) < 13) and (int(day) > 0 and int(day) < 32)

while True:
    date = input("Date: ").strip()
    try:
        m, d, y = date.split("/")

        if date_validation(m, d):
            break

    except Exception:
        try:
            _m, _d, y = date.split(" ")

            if "," in date:
                d = _d.replace(",", "")
                m = get_month_numeral(_m)

                if date_validation(m, d):
                    break
        except Exception:
            pass

print(f"{y}-{int(m):02}-{int(d):02}")
