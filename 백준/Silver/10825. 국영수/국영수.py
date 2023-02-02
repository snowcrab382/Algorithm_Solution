import sys
input = sys.stdin.readline

N = int(input())
ans = []
for i in range(N):
    student = list(input().split())
    ans.append(student)

ans.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for j in ans:
    print(j[0])