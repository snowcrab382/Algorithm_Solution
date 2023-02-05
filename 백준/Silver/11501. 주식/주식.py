import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    price = list(map(int,input().split()))
    price.reverse()
    peak = price[0]
    sum = 0

    for i in range(1,n):
        if peak < price[i]:
            peak = price[i]
            continue
        sum += peak - price[i]

    print(sum)