inp = str(input())
inp = list(inp)
for i in range(len(inp)):
    if inp[i] == "T":
        inp[i] = "U"

for letter in inp:
    print(letter, end = "")
