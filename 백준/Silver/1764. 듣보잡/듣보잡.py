import sys
input = sys.stdin.readline

N,M = map(int,input().split())
set_N = set()
set_M = set()
for _ in range(N):
    set_N.add(input().strip('\n'))
for _ in range(M):
    set_M.add(input().strip('\n'))
set_NM = list(set_N & set_M)
print(len(set_NM))
for i in sorted(set_NM):
    print(i)