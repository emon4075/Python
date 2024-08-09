try:
    X = int(input("Enter a Number: "))
except ValueError:
    print("Enter Integer MC")
else:
    print(X * X)
