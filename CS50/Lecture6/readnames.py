with open("E:/Python/CS50/Lecture6/names.txt", "r") as file:
    lines = file.readlines()


# print(lines)

for line in lines:
    # print(line,end="")
    print(line.rstrip())
