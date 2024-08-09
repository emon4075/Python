myNumber = int(input("Enter a Number: "))
if myNumber > 0 and myNumber % 2 == 0:
    print("The Number is a Positive Even Number")
elif myNumber > 0 and myNumber % 2 == 1:
    print("The Number is a Postive Odd Number")
elif myNumber < 0 and myNumber % 2 == 0:
    print("The Number is Negative Even Number")
elif myNumber < 0 and myNumber % 2 == 1:
    print("The Number is Negative Odd Number")
else:
    print("You Entered 0")
