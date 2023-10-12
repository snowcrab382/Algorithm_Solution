from collections import deque

n = int(input())
graph = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k):
    x,y = map(int,input().split())
    graph[x-1][y-1] = 1
l = int(input())
dir = [0] * 10001
for _ in range(l):
    x,c = map(str, input().split())
    dir[int(x)] = c

def check(time,dx,dy):
    if dir[time] == 'L':
        dx,dy = -dy,dx
    elif dir[time] == 'D':
        dx,dy = dy,-dx
    return dx,dy

def move(x,y):
    dx,dy = 0,1
    time = 0
    head = deque()
    tail = deque()
    head.append((x,y))
    while head:
        x,y = head.popleft()
        dx,dy = check(time,dx,dy)
        nx = x + dx
        ny = y + dy
        time += 1
        if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in tail:
            head.append((nx,ny))
            tail.append((x,y))
            if graph[nx][ny] == 0:
                tail.popleft()
            elif graph[nx][ny] == 1:
                graph[nx][ny] = 0
    print(time)

move(0,0)