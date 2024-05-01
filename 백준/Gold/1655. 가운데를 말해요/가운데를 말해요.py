import sys
import heapq
input = sys.stdin.readline

n = int(input())
left, right = [], []
for i in range(1, n+1):
    num = int(input())

    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if right and right[0] < -left[0]:
        left_max = -heapq.heappop(left)
        right_min = heapq.heappop(right)

        heapq.heappush(left, -right_min)
        heapq.heappush(right, left_max)

    print(-left[0])
