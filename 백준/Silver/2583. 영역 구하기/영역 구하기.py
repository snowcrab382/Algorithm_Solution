from collections import deque

M,N,K = map(int,input().split())
graph = [[0] * M for i in range(N)]

for _ in range(K):
    a,b,c,d = map(int,input().split())
    for i in range(a,c):
        for j in range(b,d):
            graph[i][j] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 1
    count = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx,ny))
                count += 1

    return count

paint = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            paint.append(bfs(i,j))

paint.sort()
print(len(paint))
for i in paint:
    print(i, end=' ')