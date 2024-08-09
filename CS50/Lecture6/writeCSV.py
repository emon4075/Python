import csv

Name = input("Enter Your Name: ")
Uni = input("Enter Your University: ")
Dept = input("Enter Your Department: ")

with open("E:/Python/CS50/Lecture6/Students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([Name, Uni, Dept])
