from collections import deque

n, l ,r = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def check(ground):
    visited = [[0] * n for _ in range(n)]
    unions = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q = deque([(i,j)])
                tmp = [(i,j)]
                visited[i][j] = 1
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            if l <= abs(ground[x][y] - ground[nx][ny]) <= r:
                                visited[nx][ny] = 1
                                tmp.append((nx,ny))
                                q.append((nx,ny))
                unions.append(tmp)
    return unions

def move(unions):
    for union in unions:
        sum = 0
        for x,y in union:
            sum += ground[x][y]
        people = sum // len(union)
        for x,y in union:
            ground[x][y] = people

cnt = 0
while True:
    unions = check(ground)
    if len(unions) == n**2:
        print(cnt)
        break
    move(unions)
    cnt += 1