N,K = map(int,input().split())
a = []
for i in range(1,N+1):
    if N % i == 0:
        a.append(i)
a.sort()
while len(a) < K:
    a.append(0)
print(a[K-1])