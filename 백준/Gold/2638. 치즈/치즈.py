from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    q = deque([(i,j)])
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m:
                if cheese[nx][ny]:
                    cheese[nx][ny] += 1
                if not cheese[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx,ny))



n, m = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
while True:
    visited = [[0] * m for _ in range(n)]
    bfs(0,0)
    flag = True
    for i in range(n):
        for j in range(m):
            if cheese[i][j] >= 3:
                cheese[i][j] = 0
            if cheese[i][j]:
                flag = False
                cheese[i][j] = 1

    cnt += 1
    if flag:
        print(cnt)
        break