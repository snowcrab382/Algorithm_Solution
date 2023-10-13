from collections import deque

n,m,t = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
queue = deque()

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def diffusion():
    change = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if graph[x][y] > 0:
                tmp = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m:
                        if graph[nx][ny] != -1:
                            change[nx][ny] += graph[x][y]//5
                            tmp += graph[x][y]//5
                graph[x][y] -= tmp
    for x in range(n):
        for y in range(m):
            graph[x][y] += change[x][y]

def clean_up():
    d = 1
    before = 0
    x,y = robot_top,1
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            d = (d-1)%4
            continue
        if x == robot_top and y == 0:
            break
        graph[x][y], before = before, graph[x][y]
        x,y = nx,ny

def clean_down():
    d = 1
    before = 0
    x,y = robot_bottom,1
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            d = (d+1)%4
            continue
        if x == robot_bottom and y == 0:
            break
        graph[x][y], before = before, graph[x][y]
        x,y = nx,ny


for i in range(n):
    if graph[i][0] == -1:
        robot_top = i
        robot_bottom = i+1
        break

for i in range(t):
    diffusion()
    clean_up()
    clean_down()

result = 2
for i in graph:
    result += sum(i)
print(result)