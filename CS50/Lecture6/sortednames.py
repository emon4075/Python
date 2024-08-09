names = []
with open("E:/Python/CS50/Lecture6/names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

names = sorted(names)

print(names)
