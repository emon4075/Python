class Student:
    def __init__(self, name, town):
        if name == None:
            raise NameError("Missing Name")
        if town not in ["Comilla", "Dhaka", "Mymensingh"]:
            raise NameError("Town Nai")
        else:
            self.name = name
            self.town = town

    def __str__(self):
        return f"{self.name} is from {self.town}"

    def get_name():
        name = input("Enter Name: ")
        return name

    def get_town():
        town = input("Enter Town: ")
        return town


def main():
    try:
        student = Student(Student.get_name(), Student.get_town())
        print(student)
    except:
        print("Error Occured")


if __name__ == "__main__":
    main()
