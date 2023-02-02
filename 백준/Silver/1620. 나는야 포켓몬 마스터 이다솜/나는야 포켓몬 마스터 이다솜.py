import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dict = dict()
for i in range(1,N+1):
    a = input().strip()
    dict[i] = a
    dict[a] = i
for j in range(M):
    answer = input().strip()
    if answer.isdigit():
        print(dict[int(answer)])
    else:
        print(dict[answer])