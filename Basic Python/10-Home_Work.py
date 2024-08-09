# Take Number of Grades as Input From The User as well as Grades and Average Them

Number = int(input("Enter The Number of Students: "))
ObtainedNumbers = []
Sum = 0
for i in range(0, Number, 1):
    ObtainedNumber = int(input("Enter Your Number: "))
    Sum += ObtainedNumber
    ObtainedNumbers.append(ObtainedNumber)

print("The Average is:", Sum / Number)

print("The Number Are: ")
for i in range(0, Number, 1):
    print(ObtainedNumbers[i])
