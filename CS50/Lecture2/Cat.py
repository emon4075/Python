# Press CTRL+C to get out of Infinite Loop
i = 0
while i < 5:
    print("MEOW")
    i += 1
print("FOR LOOP")
# for i in [0, 1, 2]:
#     print("MEOW")
for _ in range(3):  # If The Variable is not used then we can replace it with _
    print("MEOW")

print("Another of Priting")
print("MEOW\n" * 3, end="")
