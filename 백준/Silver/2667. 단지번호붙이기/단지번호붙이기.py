from collections import deque

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int,input())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = deque()
    graph[x][y] = 0
    queue.append((x,y))
    count = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                count += 1
                queue.append((nx,ny))
    return count

paint = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            paint.append(bfs(i,j))

paint.sort()
print(len(paint))
for i in paint:
    print(i)