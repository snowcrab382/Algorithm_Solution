import sys

input = sys.stdin.readline
n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort()
temp = 0
for i in range(n):
    if temp > rope[i] * (n-i):
        continue
    temp = rope[i] * (n-i)
print(temp)