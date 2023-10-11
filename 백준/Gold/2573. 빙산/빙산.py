from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
day = 0
check = False
queue = deque()

def bfs(x,y):
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
                elif graph[nx][ny] == 0:
                    count[x][y] += 1


while True:
    count = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    group = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                bfs(i,j)
                group += 1

    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if group == 0:
        break
    if group >= 2:
        check = True
        break
    day += 1

if check:
    print(day)
else:
    print(0)