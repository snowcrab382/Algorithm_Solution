n,m = map(int,input().split())
x,y,dir = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited[x][y] = 1
cnt = 1

while True:
    flag = 0
    for _ in range(4):
        dir = (dir+3) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                x, y = nx, ny
                flag = 1
                break
    if flag == 0:
        if graph[x-dx[dir]][y-dy[dir]] == 1:
            print(cnt)
            break
        else:
            x,y = x-dx[dir], y-dy[dir]