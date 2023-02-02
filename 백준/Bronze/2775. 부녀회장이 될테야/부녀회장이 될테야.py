T = int(input())

a = []
a.append(list(i for i in range(1,15)))
for x in range(14):
    b = []
    for y in range(1,15):
        b.append(sum(a[x][:y]))
    a.append(b)

for _ in range(T):
    k = int(input())
    n = int(input())
    print(a[k][n-1])