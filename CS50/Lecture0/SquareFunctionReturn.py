def main():
    X = int(input("Enter a Number: "))
    Result = Square(X)
    print("Result is: ", Result)


def Square(Number):
    return pow(Number, 2)

main()