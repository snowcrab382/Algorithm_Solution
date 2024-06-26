import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
check = [[0] * n for _ in range(n)]

def dfs(x,y):
    if check[x][y]:
        return check[x][y]

    check[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] > graph[x][y]:
                check[x][y] = max(check[x][y], dfs(nx,ny) + 1)
    return check[x][y]


for i in range(n):
    for j in range(n):
        if not check[i][j]:
            dfs(i,j)

result = 0
for i in check:
    result = max(result, max(i))
print(result)