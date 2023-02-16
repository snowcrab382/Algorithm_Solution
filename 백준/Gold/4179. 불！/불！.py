from collections import deque

def bfs():
    while queue:
        time, x, y = queue.popleft()
        if time > -1 and graph[x][y] != 'F' and (x == 0 or y == 0 or x == n - 1 or y == m - 1):
            return time + 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#':
                if time > -1 and graph[nx][ny] == '.':
                    graph[nx][ny] = '_'
                    queue.append((time + 1, nx, ny))

                elif time == -1 and graph[nx][ny] != 'F':
                    graph[nx][ny] = 'F'
                    queue.append((-1, nx, ny))
    return 'IMPOSSIBLE'

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
queue = deque()

graph = []
for i in range(n):
    graph.append(list(input()))
    if 'J' in graph[i]:
        queue.append((0,i,graph[i].index('J')))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'F':
            queue.append((-1,i,j))
print(bfs())