from heapq import heappush, heappop
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    max_heap = []
    min_heap = []
    visited = [0] * k
    for i in range(k):
        op, num = input().split()
        num = int(num)

        if op == 'I':
            heappush(min_heap, (num, i))
            heappush(max_heap, (-num, i))
        else:
            # 힙이 비어있지 않다면 수행
            if len(min_heap):
                # 최솟값 삭제
                if num == -1:
                    n, idx = heappop(min_heap)
                    visited[idx] = 1
                # 최댓값 삭제
                else:
                    n, idx = heappop(max_heap)
                    visited[idx] = 1

        while max_heap and visited[max_heap[0][1]]:
            heappop(max_heap)
        while min_heap and visited[min_heap[0][1]]:
            heappop(min_heap)

    if not len(min_heap):
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])

