import re

Email = input("Enter Your Email: ")
# if re.search("^[A-Za-z0-9_ ]+@[A-Za-z0-9_]+.edu$", Email):
if re.search("^(\s|\w)+@(\w|.*)+.(edu|com|net)$", Email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
