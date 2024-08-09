Amount = 50
Left = Amount
while Left > 0:
    print("Amount Due: " + str(Left))
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        Left -= coin
if Left < 0:
    Left = -Left

print("Change Owed: " + str(Left))
