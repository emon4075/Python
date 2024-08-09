from PIL import Image, ImageOps
import sys
import os


def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        format = [".jpg", ".jpeg", ".png"]
        inp = os.path.splitext(sys.argv[1])
        outp = os.path.splitext(sys.argv[2])
        if outp[1].lower() not in format:
            print("Invalid output")
            sys.exit(1)
        elif inp[1].lower() != outp[1].lower():
            print("Input and output have different extensions")
            sys.exit(1)
        else:
            edit_photo(sys.argv[1], sys.argv[2])


def edit_photo(input, output):
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        with Image.open(input) as input:
            Cropped = ImageOps.fit(input, size)
            Cropped.paste(shirt, shirt)
            Cropped.save(output)
    except FileNotFoundError:
        print(f"Input does not exist")
        sys.exit(1)


if __name__ == "__main__":
    main()
