# Lists are mutable. Sorrounded by []


def main():
    student = get_student()
    if student[0] == "Saad":
        student[1] = "Mymensingh"
    else:
        pass
    print(f"{student[0]} is from {student[1]}")


def get_student():
    name = input("Enter Name: ")
    town = input("Enter Town: ")
    return [name, town]


if __name__ == "__main__":
    main()
