N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
a.sort()
for j in range(N):
    print(a[j])