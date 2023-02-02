X = int(input())
N = int(input())
A = 0
for i in range(N):
    a, b = map(int,input().split())
    A += (a*b)
if X == A:
    print('Yes')
else:
    print('No')