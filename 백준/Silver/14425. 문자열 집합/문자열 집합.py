import sys
input = sys.stdin.readline
N,M = map(int,input().split())
S = set()
check = list()
for _ in range(N):
    S.add(input())

for _ in range(M):
    check.append(input())

count = 0
for i in check:
    if i in S:
        count += 1

print(count)