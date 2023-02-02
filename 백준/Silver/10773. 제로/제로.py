import sys
input = sys.stdin.readline

K = int(input())
num = []
for _ in range(K):
    a = int(input())
    if a != 0:
        num.append(a)
    else:
        num.pop()
print(sum(num))