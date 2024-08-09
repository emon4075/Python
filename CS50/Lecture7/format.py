import re

name = input("Enter Yout Name: ").strip()
if matches := re.search("^(.+), *(.+)$", name):  # Walrus Operator :=
    print(matches.group(1) + " " + matches.group(2))
else:
    print(name)
