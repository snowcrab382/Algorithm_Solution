from collections import deque

n,m = map(int,input().split())
graph = [list(input().split()) for _ in range(n)]
result = {0}
count = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    area = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '1':
                queue.append((nx,ny))
                graph[nx][ny] = '0'
                area += 1
    result.add(area)

for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            graph[i][j] = '0'
            bfs(i,j)
            count += 1

print(count)
print(max(result))