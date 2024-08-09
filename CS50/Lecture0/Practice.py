S = input().split()
Length = len(S)
for i in range(0, Length, 1):
    if i < Length - 1:
        print(S[i], end="")
        print("...", end="")
    else:
        print(S[i])
