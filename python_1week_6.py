inp = str(input())

S=0
for i in range(len(inp)):
    if inp[i]=="A":
        S=S+1
print(S, end=" ")

S=0
for i in range(len(inp)):
    if inp[i]=="C":
        S=S+1
print(S, end=" ")

S=0
for i in range(len(inp)):
    if inp[i]=="G":
        S=S+1
print(S, end=" ")

S=0
for i in range(len(inp)):
    if inp[i]=="T":
        S=S+1
print(S, end=" ")
