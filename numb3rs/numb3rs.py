import re

def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)
    if match is None:
        return False
    groups = match.groups()
    for group in groups:
        num = int(group)
        if num < 0 or num > 255:
            return False
    return True


