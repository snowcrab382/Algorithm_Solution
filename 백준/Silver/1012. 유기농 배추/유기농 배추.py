from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[0] * M for i in range(N)]
    for j in range(K):
        x,y = map(int,input().split())
        graph[y][x] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i,j)
                count += 1

    print(count)