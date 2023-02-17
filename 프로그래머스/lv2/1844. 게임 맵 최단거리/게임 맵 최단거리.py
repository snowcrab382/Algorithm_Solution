from collections import deque

def solution(maps):
    queue = deque()
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        if x == len(maps)-1 and y == len(maps[0])-1:
            return maps[len(maps)-1][len(maps[0])-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))
    return -1

dx = [1,-1,0,0]
dy = [0,0,1,-1]