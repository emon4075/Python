while True:
    try:
        s = input("Fraction: ").strip()
        Token = s.split("/")
        Up = int(Token[0])
        Down = int(Token[1])
        Res = round((Up / float(Down)) * 100)
        if Up > Down:
            continue
        elif Res <= 1:
            print("E", end="")
        elif Res >= 99:
            print("F", end="")
        else:
            print(int(Res), "%", sep="", end="")
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
    else:
        break
