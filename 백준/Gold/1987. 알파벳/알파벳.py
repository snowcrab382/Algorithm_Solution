import sys
input = sys.stdin.readline

def dfs(x,y,cnt):
    global max_temp
    max_temp = max(cnt,max_temp)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and visited[graph[nx][ny]] == 0:
            visited[graph[nx][ny]] = 1
            dfs(nx,ny,cnt+1)
            visited[graph[nx][ny]] = 0


dx = [1,-1,0,0]
dy = [0,0,1,-1]

max_temp = 0
r,c = map(int,input().split())
graph = [list(map(lambda a : ord(a)-65,input())) for _ in range(r)]
visited = [0]*26
visited[graph[0][0]] = 1

dfs(0,0,1)
print(max_temp)