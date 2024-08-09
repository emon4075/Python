class Student:
    def __init__(self, name, town):
        self.name = name
        self.town = town

    def get_name():
        name = input("Enter Name: ")
        return name

    def get_town():
        town = input("Enter Town: ")
        return town


def main():
    student = Student(
        Student.get_name(), Student.get_town()
    )  # Makes Object By Constructor
    print(f"{student.name} is from {student.town}")


if __name__ == "__main__":
    main()
