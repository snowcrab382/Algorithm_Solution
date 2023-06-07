n = int(input())
a = [0] * 1000001
a[1] = 1
a[2] = 2
a[3] = 3

for i in range(4,1000001):
    a[i] = (a[i-2]+a[i-1])%15746

print(a[n])