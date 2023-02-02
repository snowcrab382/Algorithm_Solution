N = int(input())
ans = list(map(int,input().split()))
count = 0
for i in ans:
    a = []
    for j in range(1,i+1):
        if i % j == 0:
            a.append(j)
    if len(a) == 2:
        count += 1
print(count)