import sys
from pyfiglet import Figlet as F

length = len(sys.argv)
if length == 1:
    s = input("Input: ")
    print(F().renderText(s))
elif length == 2:
    sys.exit(1)
else:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        Token = F().getFonts()
        if sys.argv[2] not in Token:
            sys.exit(1)
        else:
            s = input("Input: ")
            print(F(font=sys.argv[2]).renderText(s))
    else:
        sys.exit(1)
