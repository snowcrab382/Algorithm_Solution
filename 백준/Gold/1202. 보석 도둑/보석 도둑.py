import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
j = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
j.sort()
bags.sort()

result = 0
tmp = []
for bag in bags:
    while j and j[0][0] <= bag:
        heapq.heappush(tmp, -j[0][1])
        heapq.heappop(j)

    if tmp:
        result -= heapq.heappop(tmp)
print(result)