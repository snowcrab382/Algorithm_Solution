from collections import deque

dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < b and 0 <= ny < a and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))

while True:
    cnt = 0
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    graph = [list(map(int,input().split())) for _ in range(b)]
    for i in range(b):
        for j in range(a):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)