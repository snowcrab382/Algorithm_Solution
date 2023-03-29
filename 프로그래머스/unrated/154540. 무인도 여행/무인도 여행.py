from collections import deque

def solution(maps):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(len(maps)):
        maps[i] = list(maps[i])
        
    answer = []
    r,c = len(maps),len(maps[0])
    visited = [[0]*c for _ in range(r)]
    
    def bfs(x,y):
        count = 0
        queue = deque()
        queue.append((x,y))
        visited[x][y] = 1
        count += int(maps[x][y])

        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] != 'X' and not visited[nx][ny]:
                    count += int(maps[nx][ny])
                    queue.append((nx,ny))
                    maps[nx][ny] = 'X'
        answer.append(count)
        
    for i in range(r):
        for j in range(c):
            if maps[i][j] != 'X':
                bfs(i,j)
    
    if len(answer):
        answer.sort()
        return answer
    else:
        return [-1]
    
    