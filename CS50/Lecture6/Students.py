import csv

with open("E:/Python/CS50/Lecture6/Students.csv") as file:
    reader = csv.reader(file)
    for list in reader:
        print(f"Name is : {list[0]} studying in {list[1]} in {list[2]}")
