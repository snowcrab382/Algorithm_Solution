d = [i for i in range(1,1001)]
d.insert(0, 1)

for i in range(1,len(d)):
    d[i] = d[i-1] * d[i]

n,k = map(int,input().split())
print((d[n] // d[n-k] // d[k]) % 10007)