def main():
    number = get_Number()
    Meow(number)


def get_Number():
    while True:
        number = int(input("Enter a Number : "))
        if number > 0:
            break
    return number


def Meow(N):
    for _ in range(N):
        print("MEOW")


main()
