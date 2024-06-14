import heapq
import sys
input = sys.stdin.readline

MAX = sys.maxsize

n, k = map(int,input().split())
cost = [MAX] * (100001)
cost[n] = 0
heap = [(cost[n], n)]
answer = []

while heap:
    tmp, idx = heapq.heappop(heap)

    if idx == k:
        answer.append(tmp)

    for next in (idx-1, idx+1, idx*2):
        if 0 <= next <= 100000:
            if tmp + 1 <= cost[next]:
                cost[next] = min(cost[next], tmp + 1)
                heapq.heappush(heap, (cost[next], next))
min_cost = min(answer)
print(min_cost)
print(answer.count(min_cost))