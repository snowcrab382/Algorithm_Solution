from collections import deque

dx= [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C and graph[nz][nx][ny] == '.':
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz,nx,ny))

while True:
    L, R, C = map(int, input().split())
    graph = []
    if L == 0 and R == 0 and C == 0:
        break
    else:
        queue = deque()
        for i in range(L):
            floor = []
            for j in range(R):
                floor.append(list(input()))
            input()
            graph.append(floor)

        a, b, c = 0, 0, 0
        for i in range(L):
            for j in range(R):
                for k in range(C):
                    if graph[i][j][k] == 'S':
                        graph[i][j][k] = 0
                        queue.append((i, j, k))
                    if graph[i][j][k] == 'E':
                        a, b, c = i, j, k
                        graph[i][j][k] = '.'

        bfs()

        if graph[a][b][c] == '.':
            print('Trapped!')
        else:
            print(f'Escaped in {graph[a][b][c]} minute(s).')