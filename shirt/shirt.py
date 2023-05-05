import sys, os
from PIL import Image, ImageOps

def main():
    input_file, output_file = check_args()

    check_extention(input_file, output_file)
    update_photo(input_file,output_file)


def check_args():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    else:
        return sys.argv[1], sys.argv[2]


def check_extention(input_file,output_file):
    if not input_file.split('.')[1].lower() in ['jpg', 'jpeg', 'png']:
        sys.exit("Invalid input file")

    if  not output_file.split('.')[1].lower() in ['jpg', 'jpeg', 'png']:
        sys.exit("Invalid output file")

    if input_file.split('.')[1].lower() != output_file.split('.')[1].lower():
        sys.exit("Input and output files must have the same extension")


def update_photo(input_file,output_file):
    try:
        input_image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = Image.open("shirt.png")

    input_image = ImageOps.fit(input_image, shirt.size)

    input_image.paste(shirt, shirt)

    input_image.save(output_file)


if __name__ == '__main__':
    main()