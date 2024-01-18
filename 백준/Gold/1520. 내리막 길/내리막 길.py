import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

def dfs(x,y):
    if x == m-1 and y == n-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    route = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[x][y] > graph[nx][ny]:
            route += dfs(nx,ny)

    dp[x][y] = route
    return dp[x][y]

print(dfs(0,0))