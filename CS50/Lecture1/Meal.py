def main():
    S = input("What time is it? ").strip()
    T = convert(S)
    if T >= 7 and T <= 8:
        print("breakfast time")
    elif T >= 12 and T <= 13:
        print("lunch time")
    elif T >= 18 and T <= 19:
        print("dinner time")


def convert(time):
    Token = time.split(":")
    Hour = float(Token[0])
    Minute = float(Token[1])
    Minute = Minute / 60
    return Hour + Minute


if __name__ == "__main__":
    main()
