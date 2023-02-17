from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def solution(rectangle,characterX,characterY,itemX,itemY):
    graph = [[-1] * 102 for _ in range(102)]
    visited = [[0] * 102 for _ in range(102)]
    for i in rectangle:
        for x in range(i[0]*2,i[2]*2+1):
            for y in range(i[1]*2,i[3]*2+1):
                if i[0]*2 < x < i[2]*2 and i[1]*2 < y < i[3]*2:
                    graph[x][y] = 0
                elif graph[x][y] != 0:
                    graph[x][y] = 1

    queue = deque()
    queue.append((characterX*2, characterY*2))
    visited[characterX*2][characterY*2] = 1
    while queue:
        x,y = queue.popleft()
        if x == itemX*2 and y == itemY*2:
            return visited[x][y] // 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))