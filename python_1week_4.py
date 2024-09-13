N = int(input())
data = [0]*N
for i in range(N):
    data[i]=int(input())
data.sort()

j=N

for i in range(N):
    if data[i]>=0:
        j=i
        break

for i in range(j, N):
    print(data[i], end=" ")
for i in range(j-1, -1, -1):
    print(data[i], end=" ")
