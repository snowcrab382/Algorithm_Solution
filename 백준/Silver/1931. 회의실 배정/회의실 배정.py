import sys

input = sys.stdin.readline
n = int(input())
table = []
for _ in range(n):
    table.append(list(map(int,input().split())))

table.sort(key = lambda x : (x[1],x[0]))

temp = 0
cnt = 0
for i in range(n):
    if temp > table[i][0]:
        continue
    cnt += 1
    temp = table[i][1]

print(cnt)