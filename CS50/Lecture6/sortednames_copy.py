with open("E:/Python/CS50/Lecture6/names.txt", "r") as file:
    for line in sorted(file, reverse=True):
        print(line, end="")
