X = int(input("Enter The First Number: "))
Y = int(input("Enter The Second Number: "))

try:
    print("Division is: ", X / Y)
except ZeroDivisionError:
    print("Can't Divide By Zero")
