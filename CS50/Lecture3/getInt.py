def get_int():
    while True:
        try:
            X = int(input("Enter an Integer: "))
        except ValueError:
            print("Not an Integer: ")
            # continue
            # pass
        else:
            break
    return X


def main():
    Y = get_int()
    print("Entered Integer is: ", Y)


main()
