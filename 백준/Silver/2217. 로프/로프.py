import sys
input = sys.stdin.readline

N = int(input())
a = []
result = 0
for i in range(N):
    a.append(int(input()))
a.sort()
for j in range(N):
    if a[j]*(N-j) > result:
        result = a[j]*(N-j)
print(result)