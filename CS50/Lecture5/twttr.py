def main():
    S = input("Input: ").strip()
    print("Output:", shorten(S))


def shorten(word):
    newString = ""
    for i in word:
        if i.lower() not in "aeiou":
            newString += i
    return newString


if __name__ == "__main__":
    main()
