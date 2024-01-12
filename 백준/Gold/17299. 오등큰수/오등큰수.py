from collections import Counter

n = int(input())
a = list(map(int,input().split()))
f = Counter(a)

result = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and f[a[stack[-1]]] < f[a[i]]:
        result[stack.pop()] = a[i]
    stack.append(i)

print(*result)