A,B = map(int,input().split())
a = []
for i in range(1,46):
    for j in range(i):
        a.append(i)
print(sum(a[A-1:B]))