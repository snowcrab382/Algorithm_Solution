import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

result = 0

def dfs(x, y, tmp, cnt):
    global result
    if cnt == 4:
        result = max(result, tmp)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, tmp+graph[nx][ny], cnt+1)
            visited[nx][ny] = False

def remains(x, y):
    global result
    for i in range(4):
        tmp = graph[x][y]
        for j in range(3):
            t = (i+j) % 4
            nx = x + dx[t]
            ny = y + dy[t]

            if not (0 <= nx < n and 0 <= ny < m):
                tmp = 0
                break
            tmp += graph[nx][ny]
        result = max(result, tmp)

for x in range(n):
    for y in range(m):
        visited[x][y] = True
        dfs(x, y, graph[x][y], 1)
        visited[x][y] = False

        remains(x, y)
print(result)