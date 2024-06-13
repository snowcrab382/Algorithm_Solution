import heapq
import sys

MAX = sys.maxsize

dx = [1,-1,0,0]
dy = [0,0,1,-1]

cnt = 0
while True:
    n = int(input())
    if not n:
        break
    cnt += 1

    graph = [list(map(int,input().split())) for _ in range(n)]
    dist = [[MAX] * n for _ in range(n)]
    dist[0][0] = graph[0][0]
    heap = []
    heapq.heappush(heap, (dist[0][0], 0, 0))

    while heap:
        distance, x, y = heapq.heappop(heap)

        if x == n-1 and y == n-1:
            print(f'Problem {cnt}: {distance}')
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist[x][y] + graph[nx][ny]
                if dist[nx][ny] > cost:
                    dist[nx][ny] = cost
                    heapq.heappush(heap, (dist[nx][ny], nx, ny))
