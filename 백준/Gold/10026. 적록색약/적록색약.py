from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(visit,x,y):
    queue = deque()
    queue.append((x,y))
    visit[x][y] = 1
    current_color = graph[x][y]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == current_color:
                if not visit[nx][ny]:
                    visit[nx][ny] = 1
                    queue.append((nx,ny))

n = int(input())
graph = [list(input()) for _ in range(n)]
visit,visit_RG = [[0] * n for _ in range(n)],[[0] * n for _ in range(n)]
cnt,cnt_RG = 0,0

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(visit,i,j)
            cnt += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visit_RG[i][j]:
            bfs(visit_RG,i,j)
            cnt_RG += 1

print(cnt,cnt_RG)