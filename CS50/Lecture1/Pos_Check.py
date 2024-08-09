def main():
    X = int(input("Enter a Number: "))
    if Check(X):
        print("Positive Number")
    else:
        print("Negative Number")


def Check(I):
    if I > 0:
        return True
    else:
        return False


main()
