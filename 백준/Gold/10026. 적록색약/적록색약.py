from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs_R(visit,x,y):
    queue_R = deque()
    queue_R.append((x,y))
    visit[x][y] = 1
    while queue_R:
        x,y = queue_R.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 'R':
                if not visit[nx][ny]:
                    visit[nx][ny] = 1
                    queue_R.append((nx,ny))

def bfs_G(visit,x,y):
    queue_G = deque()
    queue_G.append((x,y))
    visit[x][y] = 1
    while queue_G:
        x,y = queue_G.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 'G':
                if not visit[nx][ny]:
                    visit[nx][ny] = 1
                    queue_G.append((nx,ny))

def bfs_B(visit,x,y):
    queue_B = deque()
    queue_B.append((x,y))
    visit[x][y] = 1
    while queue_B:
        x,y = queue_B.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 'B':
                if not visit[nx][ny]:
                    visit[nx][ny] = 1
                    queue_B.append((nx,ny))
n = int(input())
graph = [list(input()) for _ in range(n)]
visit,visit_RG = [[0] * n for _ in range(n)],[[0] * n for _ in range(n)]
cnt,cnt_RG = 0,0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R' and not visit[i][j]:
            bfs_R(visit,i,j)
            cnt += 1
        if graph[i][j] == 'G' and not visit[i][j]:
            bfs_G(visit,i,j)
            cnt += 1
        if graph[i][j] == 'B' and not visit[i][j]:
            bfs_B(visit,i,j)
            cnt += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R' and not visit_RG[i][j]:
            bfs_R(visit_RG,i,j)
            cnt_RG += 1
        if graph[i][j] == 'B' and not visit_RG[i][j]:
            bfs_B(visit_RG,i,j)
            cnt_RG += 1

print(cnt,cnt_RG)