N = int(input())

while N>9:
    S = 0
    for i in range(8, -1, -1):
        dig = N // (10**i)
        S = S + dig
        N = N - dig*(10**i)
    N = S

print(N)
