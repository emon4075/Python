S = input("Input: ").strip()
newString = ""

for i in S:
    if i.lower() not in "aeiou":
        newString += i

print("Output:", newString)
