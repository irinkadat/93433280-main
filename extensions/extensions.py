
def main():
    file = input("File name:")

    print(determine(file))


def determine(result):
    extensions = {
    "gif" : "image",
    "jpeg" : "image",
    "jpg" : "image",
    "png" : "image",
    "pdf" : "application",
    "text": "plain",
    "zip" : "application"
    }

    result = result.strip().lower().split('.')

    if len(result)<2 :
        return "application/octet-stream"
    if len(result)>2:
        return  f"{extensions[result[-1]]}/{result[-1]}"

    if result[1] == 'jpg':
        return f"{extensions['jpeg']}/jpeg"

    if result[1] == 'txt':
        return f"text/{extensions['text']}"

    if result[1] not in extensions:
        return "application/octet-stream"

    if result[1] in extensions:
        return  f"{extensions[result[1]]}/{result[1]}"




if __name__ == "__main__":
    main()
