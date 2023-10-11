from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[[0,0] for _ in range(m)] for _ in range(n)]

def bfs(x,y,breakable):
    queue = deque()
    queue.append((x,y,breakable))
    visited[x][y][breakable] = 1
    while queue:
        x,y,breakable = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][breakable]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][breakable] == 0:
                    queue.append((nx,ny,breakable))
                    visited[nx][ny][breakable] = visited[x][y][breakable] + 1
                if graph[nx][ny] == 1 and breakable == 1:
                    queue.append((nx,ny,breakable-1))
                    visited[nx][ny][breakable-1] = visited[x][y][breakable] + 1
    return -1

print(bfs(0,0,1))