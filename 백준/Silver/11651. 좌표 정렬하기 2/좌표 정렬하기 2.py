import sys
input = sys.stdin.readline

N = int(input())
a = []
for _ in range(N):
    a.append(list(map(int,input().split())))

a.sort()
a.sort(key = lambda x: x[1])
for x,y in a:
    print(x,y)