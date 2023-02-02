import sys
input = sys.stdin.readline

N = int(input())
a=[]
for _ in range(N):
    a.append(list(input().split()))
a.sort(key = lambda x: int(x[0])) 
for x,y in a:
    print(x,y)