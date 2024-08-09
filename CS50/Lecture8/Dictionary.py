def main():
    student = get_student()
    if student["name"] == "Saad":
        student["town"] = "Mymensingh"
    else:
        pass
    print(f"{student['name']} is from {student['town']}")


def get_student():
    student = {}
    student["name"] = input("Enter Name: ")
    student["town"] = input("Enter Town: ")
    return student


if __name__ == "__main__":
    main()
