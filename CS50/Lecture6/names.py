name = input("Enter Your Name:")
# file = open("E:/Python/CS50/Lecture6/names.txt", "w") --> Write
# file = open("E:/Python/CS50/Lecture6/names.txt", "a") --> Append
# file.write(f"{name}\n")
# file.close()

with open("E:/Python/CS50/Lecture6/names.txt", "a") as file:
    file.write(f"{name}\n")
