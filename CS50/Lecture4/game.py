import random
import sys

while True:
    try:
        L = int(input("Level: "))
        if L > 0:
            break
    except ValueError:
        continue

rand = random.randint(1, L)

while True:
    try:
        G = int(input("Guess: "))
        if G <= 0:
            continue
        if G < rand:
            print("Too small!")
        elif G > rand:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit(0)
    except ValueError:
        continue
