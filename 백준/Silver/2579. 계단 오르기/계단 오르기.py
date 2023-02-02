n = int(input())
d = [0] * (n+1)
num = [0]
tot = 0
for _ in range(n):
    num.append(int(input()))
    tot += num[-1]

if n <= 2:
    print(tot)
    exit(0)
d[1] = num[1]
d[2] = num[2]
d[3] = num[3]

for i in range(4,n+1):
    d[i] = num[i] + min(d[i-2],d[i-3])

print(tot-min(d[n-1],d[n-2]))