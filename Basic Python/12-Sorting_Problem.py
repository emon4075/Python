number_Elements = int(input("Enter The Number of Elements: "))
Elements = []
for i in range(0, number_Elements, 1):
    X = int(input())
    Elements.append(X)

for i in range(0, number_Elements - 1, 1):
    for j in range(i + 1, number_Elements, 1):
        if Elements[i] < Elements[j]:
            Temp = Elements[i]
            Elements[i] = Elements[j]
            Elements[j] = Temp

print("Descending Order: ", Elements)
