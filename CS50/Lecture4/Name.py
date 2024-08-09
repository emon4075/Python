import sys

if len(sys.argv) < 2:
    print("Too Few Arguments")
else:
    for arg in sys.argv[1 : len(sys.argv)]:
        print("Hello", arg)
