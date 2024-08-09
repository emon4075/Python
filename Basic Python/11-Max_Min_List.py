myGrades = []
Number = int(input("Enter The Number of Grades: "))
for i in range(0, Number, 1):
    X = int(input("Enter Your Grade: "))
    myGrades.append(X)
print("Your Grades Are: ", myGrades)
Maxi = -1
Mini = 101
for i in range(0, Number, 1):
    if Mini > myGrades[i]:
        Mini = myGrades[i]
    elif Maxi < myGrades[i]:
        Maxi = myGrades[i]
print("Maximum Value is:", Maxi)
print("Minimum Value is:", Mini)
