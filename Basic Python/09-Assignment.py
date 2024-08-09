Number = int(input("Enter The Number of Grades That You Want to Store: "))
myGrades = []
for i in range(0, Number, 1):
    myGrade = input("Enter Your Grade: ")
    myGrades.append(myGrade)

# for myGrade in myGrades:
#     print(myGrade)

for i in range(0, Number, 1):
    print(myGrades[i])
