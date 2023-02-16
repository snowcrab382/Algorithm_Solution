from collections import deque
import sys

def bfs():
    while queue:
        time,x,y = queue.popleft()
        if time > -1 and graph[x][y] != '*' and (x == 0 or x == h-1 or y == 0 or y == w-1):
            return time+1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != '#':
                if time > -1 and graph[nx][ny] == '.':
                    graph[nx][ny] = '_'
                    queue.append((time+1,nx,ny))
                elif time == -1 and graph[nx][ny] != '*':
                    graph[nx][ny] = '*'
                    queue.append((-1,nx,ny))
    return 'IMPOSSIBLE'

dx = [1,-1,0,0]
dy = [0,0,1,-1]

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    w,h = map(int,input().split())
    graph = []
    queue = deque()
    for i in range(h):
        graph.append(list(input().rstrip()))
        if '@' in graph[i]:
            queue.append((0,i,graph[i].index('@')))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                queue.append((-1,i,j))
    print(bfs())