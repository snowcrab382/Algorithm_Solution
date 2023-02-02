import sys
input = sys.stdin.readline

N = int(input())
set_N = list(map(int,input().split()))
set_N = set(set_N)

M = int(input())
set_M = list(map(int,input().split()))
for i in set_M:
    if i in set_N:
        print(1)
    else:
        print(0)