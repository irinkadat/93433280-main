import re
def main():
    html = input("input html: ")
    parse(parse(html))


def parse(html):
    pattern = r'<iframe.*?src="(https?://)?(www\.)?(youtube\.com|youtu\.be)/embed/([a-zA-Z0-9_-]+)".*?>'
    match = re.search(pattern, html)
    if match:
        video_id = match.group(4)
        return f"https://youtu.be/{video_id}"




if __name__=="__main__":
    main()