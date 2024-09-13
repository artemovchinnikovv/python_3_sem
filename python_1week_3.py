data = [float(value) for value in input().split()]
# N наход, M нужный, K лифт, Ta прох лиф, Tb откр и закр, Tc прох пеш
N = int (data[0])
M = int (data[1])
K = int (data[2])
Ta = float (data[3])
Tb = float (data[4])
Tc = float (data[5])

T_el = (abs(N-K)+abs(N-M))*Ta+Tb*3
T_st = Tc*abs(N-M)

if (T_st >= T_el):
    print("elevator")
else:
    print("stairs")
