n = int(input())
a = list(map(int,input().split()))
a_reversed = a[::-1]

ascend = [1] * n
descend = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            ascend[i] = max(ascend[i], ascend[j]+1)

        if a_reversed[i] > a_reversed[j]:
            descend[i] = max(descend[i], descend[j]+1)

descend = descend[::-1]
result = [ascend[i] + descend[i] for i in range(n)]

print(max(result)-1)