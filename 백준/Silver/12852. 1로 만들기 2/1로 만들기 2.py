n = int(input())
d = [0] * 1000001
pre = [0] * 1000001

for i in range(2,n+1):
    d[i] = d[i-1] + 1
    pre[i] = i-1
    if i % 2 == 0 and d[i] > d[i//2]+1:
        d[i] = d[i//2]+1
        pre[i] = i//2
    if i % 3 == 0 and d[i] > d[i//3]+1:
        d[i] = d[i//3]+1
        pre[i] = i//3
print(d[n])
tmp = n
while True:
    print(tmp, end=' ')
    if tmp == 1:
        break
    tmp = pre[tmp]