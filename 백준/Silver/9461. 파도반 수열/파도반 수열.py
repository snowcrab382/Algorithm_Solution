d = [0] * 101
d[1],d[2],d[3],d[4],d[5] = 1,1,1,2,2
for i in range(6,101):
    d[i] = d[i-1] + d[i-5]

T = int(input())
for i in range(T):
    n = int(input())
    print(d[n])