from collections import deque
import copy

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph_copy[x][y] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph_copy[nx][ny] != 0:
                graph_copy[nx][ny] = 0
                queue.append((nx,ny))

result = []
for a in range(1,101):
    graph_copy = copy.deepcopy(graph)
    for i in range(N):
        for j in range(N):
            if graph_copy[i][j] <= a:
                graph_copy[i][j] = 0

    count = 0
    for i in range(N):
        for j in range(N):
            if graph_copy[i][j] != 0:
                bfs(i,j)
                count += 1
    result.append(count)
if max(result) == 0:
    print(1)
else:
    print(max(result))