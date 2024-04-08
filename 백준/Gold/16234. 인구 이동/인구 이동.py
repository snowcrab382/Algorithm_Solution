from collections import deque

n, l, r = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def check(ground):
    visited = [[0] * n for _ in range(n)]
    unions = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union = [(i, j)]
                q = deque([(i, j)])
                visited[i][j] = 1
                while q:
                    x, y = q.popleft()
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            if l <= abs(ground[x][y] - ground[nx][ny]) <= r:
                                visited[nx][ny] = 1
                                q.append((nx, ny))
                                union.append((nx, ny))
                unions.append(union)
    return unions

def move(unions):
    for union in unions:
        total = 0
        for x,y in union:
            total += ground[x][y]
        people = total // len(union)
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