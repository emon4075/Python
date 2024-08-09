import sys

try:
    print("Current Python Program:", sys.argv[0])
    print("My Name is:", sys.argv[1])
    print("My Name is:", sys.argv[2])
except Exception:
    print("Not a Valid Argument")
finally:
    print("Hello World")
