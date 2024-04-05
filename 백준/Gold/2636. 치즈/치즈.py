from collections import deque

n, m = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    q = deque([(x,y)])
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if cheese[nx][ny]:
                    cheese[nx][ny] = 0
                    cnt += 1
                else:
                    q.append((nx,ny))
    return cnt

time = 0
cnt = 0
while True:
    tmp = dfs(0,0)
    if tmp == 0:
        print(time)
        print(cnt)
        break
    else:
        time += 1
        cnt = tmp