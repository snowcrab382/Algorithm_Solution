M = int(input())
N = int(input())
a= []
for i in range(M,N+1):
    b = []
    for j in range(1,i+1):
        if i % j == 0:
            b.append(j)
    if len(b) == 2:
        a.append(i)
if len(a) != 0:
    print(sum(a))
    print(min(a))
else:
    print('-1')