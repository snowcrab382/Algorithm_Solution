import sys
input = sys.stdin.readline

N = int(input())
a=[]
for i in range(N):
    b=list(map(int,input().split()))
    a.append(b)
for x,y in sorted(a):
    print(x,y)