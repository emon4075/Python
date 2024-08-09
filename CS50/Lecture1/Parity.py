def main():
    x = int(input("Enter Your Number: "))
    if Check(x):
        print("Even")
    else:
        print("Odd")


def Check(N):
    if N % 2 == 0:
        return True
    else:
        return False
    # return True if N % 2 == 0 else False
    # return N % 2 == 0


main()
