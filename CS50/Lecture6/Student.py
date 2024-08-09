with open("E:\Python\CS50\Lecture6\Student.csv", "r") as file:
    for line in file:
        name, uni = line.rstrip().split(",")
        print(f"Name {name} in {uni}")
