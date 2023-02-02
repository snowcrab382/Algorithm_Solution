import sys
from collections import deque

input = sys.stdin.readline
M,N,H = map(int,input().split())
graph = []
queue = deque([])

for i in range(H):
    floor = []
    for j in range(N):
        floor.append(list(map(int,input().split())))
        for k in range(M):
            if floor[j][k] == 1:
                queue.append((i,j,k))
    graph.append(floor)

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and graph[nz][nx][ny] == 0:
                queue.append((nz, nx, ny))
                graph[nz][nx][ny] = graph[z][x][y] + 1


bfs()
result = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        result = max(result, max(j))

print(result -1)