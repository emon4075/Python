import csv

Name = input("Enter Your Name: ")
Uni = input("Enter Your University: ")
Dept = input("Enter Your Department: ")

with open("E:/Python/CS50/Lecture6/NEW_Student.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Names", "University", "Department"])
    writer.writeheader()
    writer.writerow({"Names": Name, "University": Uni, "Department": Dept})
