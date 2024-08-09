Greet = input("Greeting: ").lower().strip()
if "hello" in Greet:
    print("$0")
elif Greet[0] == "h":
    print("$20")
else:
    print("$100")
