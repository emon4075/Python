Number = int(input("Enter The Number of Elements: "))
i = 0
Elements = []
print("Enter The Elemnets: ")
while i < Number:
    X = int(input())
    Elements.append(X)
    i = i + 1
print("The Elements Are: ")
i = 0
while i < Number:
    print(Elements[i])
    i = i + 1
