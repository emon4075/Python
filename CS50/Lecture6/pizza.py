from tabulate import tabulate as t
import sys
import csv

table = []


def main():
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        file_name = sys.argv[1]
        if not file_name.endswith(".csv"):
            print("Not a CSV file")
            sys.exit(1)
        else:
            solve(file_name)


def solve(file_name):
    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                table.append(row)
            print(t(table, headers=headers, tablefmt="grid"))

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


if __name__ == "__main__":
    main()
