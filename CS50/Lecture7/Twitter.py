import re

# ? Makes it optional
url = input("Enter The URL: ")
userName = re.sub("^(https?://)?(www\.)?twitter\.com/", "", url)
print(userName)
