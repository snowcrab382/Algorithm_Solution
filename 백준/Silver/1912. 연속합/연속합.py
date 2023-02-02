n = int(input())
a = list(map(int,input().split()))
d = [0] * 100010
for i in range(1,len(a)+1):
    d[i] = a[i-1]

for i in range(1,n+1):
    d[i] = max(d[i], d[i-1] + a[i-1])
print(max(d[1:n+1]))