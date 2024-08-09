# Ask User For Their Name
name = input("Enter Your Name: ")


# Hello To The User
print("Hello", name)
# Hello As Concatanation
print("Welcome " + name)


# print(*objects, sep=' ', end='\n', file=None, flush=False)
# This Will Print Without New Line
print("Hello ", end="")
print(name)


# This Will Have a Tab After The Hello String
print("Hello ", end="\t")
print(name)

# Now This Will Change The Separator To @ From a Space
print("Hello", name, sep="@")


# Name With Quatation
print("Hello", '"Emon"')