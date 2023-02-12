from collections import deque
import sys

input = sys.stdin.readline
n,m = map(int,input().split())
graph = []
queue = deque()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(m):
    line = list(map(int,input().split()))
    graph.append(line)
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i,j))

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

bfs()
result = 0

for i in graph:
    for j in i:
        if j== 0:
            print(-1)
            exit(0)
    result = max(result,max(i))
print(result-1)