camel = input("camelCase: ").strip()
modified_string = ""

for i in camel:
    if i.isupper():
        modified_string += "_" + i.lower()
    else:
        modified_string += i

print("snake_case:", modified_string)
