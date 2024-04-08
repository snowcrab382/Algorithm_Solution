from collections import deque

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    q = deque([(i,j)])
    visited[i][j] = 1
    tmp = []
    while q:
        x,y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    tmp.append((nx,ny))
                else:
                    q.append((nx,ny))
                visited[nx][ny] = 1

    for r,c in tmp:
        graph[r][c] = 0
    return len(tmp)

cnt = 0
cheese = 0
while True:
    visited = [[0] * m for _ in range(n)]
    tmp = bfs(0,0)
    if tmp == 0:
        print(cnt)
        print(cheese)
        break
    cheese = tmp
    cnt += 1