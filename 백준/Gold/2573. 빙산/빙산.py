from collections import deque
import sys

input = sys.stdin.readline

def melting():
    while queue:
        cnt = 0
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                cnt += 1
        melt.append((x,y,cnt))

def bfs(x,y):
    check = deque()
    check.append((x,y))
    while check:
        x,y = check.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] != 0:
                visited[nx][ny] = True
                check.append((nx,ny))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
queue = deque()
year = 0

for i in range(1,n-1):
    for j in range(1,m-1):
        if graph[i][j] != 0:
            queue.append((i,j))

while queue:
    melt = []
    visited = [[False] * m for _ in range(n)]
    group = 0
    year += 1

    melting()
    for i,j,k in melt:
        if graph[i][j] - k <= 0:
            graph[i][j] = 0
        else:
            graph[i][j] -= k
            queue.append((i,j))

    for i in range(1,n-1):
        for j in range(1,m-1):
            if graph[i][j] != 0 and not visited[i][j]:
                bfs(i,j)
                visited[i][j] = True
                group += 1
    if group > 1:
        print(year)
        exit(0)
print(0)