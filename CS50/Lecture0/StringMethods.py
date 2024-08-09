# Removes Whitespaces From String
name = input("Enter Your Name:").strip().title()
# name = name.strip().title()
print("Hello", name)


# This Will Capitalize Only The Firt Letter
name = input("Enter Your Full Name: ")
name = name.capitalize()  # Abdullah al mamun emon
print(name)


# Capitalizes The Word Beginings
name = name.title()  # Abdullah Al Mamun Emon
print(name)


# Split Function - Sperates Strings Based On Given Separator
name = input("Enter Your Name: ")
first, second = name.split(" ")
print("First Name: " + first)
print("Last Name:", second)
