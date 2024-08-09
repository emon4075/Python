from emoji import emojize as emj

s = input("Input: ")
o = emj(s, language="alias")
print("Output:", o)
