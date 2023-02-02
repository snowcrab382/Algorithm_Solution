N,M = map(int,input().split())
a = list(map(int,input().split()))
l = len(a)
ans = 0
for i in range(l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            if(a[i]+a[j]+a[k] > M):
                continue
            else:
                ans = max(ans, a[i] + a[j] + a[k])
print(ans)