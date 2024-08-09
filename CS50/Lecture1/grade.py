mark = int(input("Enter Your Marks: "))
if mark >= 90 and mark <= 100:
    print("Grade: A+")
elif 80 <= mark < 90:  # The Logic Can be written as this
    print("Grade: B+")
else:
    print("Fail")
