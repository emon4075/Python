def main():
    S = input().split()
    convert(S)


def convert(S):
    Length = len(S)
    Result = ""
    for i in range(0, Length, 1):
        if S[i] == ":)":
            Result += "🙂"
            Result += " "
        elif S[i] == ":(":
            Result += "☹️"
            Result += " "
        else:
            Result += S[i]
            Result += " "
    print(Result, sep="", end="")


main()
