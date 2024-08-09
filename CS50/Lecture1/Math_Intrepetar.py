S = input("Expression: ").lower().strip().split()
X = float(S[0])
Z = float(S[2])
Y = S[1]
if Y == "+":
    print(f"{X+Z:.1F}")
elif Y == "-":
    print(f"{X-Z:.1F}")
elif Y == "+*":
    print(f"{X*Z:.1F}")
else:
    print(f"{X/Z:.1F}")
