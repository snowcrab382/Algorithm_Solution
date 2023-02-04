import sys

input = sys.stdin.readline
n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort()
temp = rope[0] * n
for i in range(1,n):
    if temp > rope[i] * (n-i):
        continue
    temp = rope[i] * (n-i)

print(temp)