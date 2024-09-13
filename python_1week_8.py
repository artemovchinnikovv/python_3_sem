inp = str(input())
inp = list(inp)
for i in range(len(inp)):
    if inp[i] == "A":
        inp[i] = "T"
    else: 
        if inp[i] == "T":
            inp[i] = "A"
    if inp[i] == "C":
        inp[i] = "G"
    else: 
        if inp[i] == "G":
            inp[i] = "C"
inp.reverse()
for letter in inp:
    print(letter, end = "")
