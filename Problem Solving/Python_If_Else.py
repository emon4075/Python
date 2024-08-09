# https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
Number = int(input())
if Number % 2 == 1:
    print("Weird")
else:
    if Number >= 2 and Number <= 5:
        print("Not Weird")
    elif Number >= 6 and Number <= 20:
        print("Weird")
    else:
        print("Not Weird")
