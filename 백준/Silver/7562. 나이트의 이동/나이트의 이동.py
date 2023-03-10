from collections import deque

dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]

def bfs(x,y):
    queue = deque()
    graph[x][y] = 1
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        if x == stop_x and y == stop_y:
            return graph[x][y]-1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

T = int(input())
for _ in range(T):
    l = int(input())
    graph = [[0] * l for _ in range(l)]
    start_x,start_y = map(int,input().split())
    stop_x, stop_y = map(int,input().split())

    print(bfs(start_x,start_y))