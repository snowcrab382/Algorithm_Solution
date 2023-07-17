import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    tmp = [100001, 100001]
    count = 0
    check = []

    for _ in range(n):
        rank = list(map(int,input().split()))
        check.append(rank)

    check.sort(key=lambda x : (x[0],x[1]))

    for i,j in check:
        if i > tmp[0] and j > tmp[1]:
            continue
        else:
            tmp[0],tmp[1] = i,j
            count += 1
    print(count)