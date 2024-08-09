import sys


def main():
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        file_name = sys.argv[1]
        if not file_name.endswith(".py"):
            print("Not a Python file")
            sys.exit(1)
        else:
            print(solve(file_name))


def solve(file_name):
    try:
        Count = 0
        with open(file_name, "r") as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line and not stripped_line.startswith("#"):
                    Count += 1
            return Count
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


if __name__ == "__main__":
    main()
