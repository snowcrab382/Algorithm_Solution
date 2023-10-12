from collections import deque

n,m,x,y,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
move = deque(list(map(int,input().split())))

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

def roll(dice,dir):
    rolled_dice = [0,0,0,0,0,0]
    if dir == 1:
        rolled_dice[0] = dice[0]
        rolled_dice[2] = dice[1]
        rolled_dice[3] = dice[2]
        rolled_dice[5] = dice[3]
        rolled_dice[4] = dice[4]
        rolled_dice[1] = dice[5]
    elif dir == 2:
        rolled_dice[0] = dice[0]
        rolled_dice[5] = dice[1]
        rolled_dice[1] = dice[2]
        rolled_dice[2] = dice[3]
        rolled_dice[4] = dice[4]
        rolled_dice[3] = dice[5]
    elif dir == 3:
        rolled_dice[5] = dice[0]
        rolled_dice[1] = dice[1]
        rolled_dice[0] = dice[2]
        rolled_dice[3] = dice[3]
        rolled_dice[2] = dice[4]
        rolled_dice[4] = dice[5]
    else:
        rolled_dice[2] = dice[0]
        rolled_dice[1] = dice[1]
        rolled_dice[4] = dice[2]
        rolled_dice[3] = dice[3]
        rolled_dice[5] = dice[4]
        rolled_dice[0] = dice[5]
    return rolled_dice

def bfs(x,y):
    dice = [0,0,0,0,0,0]
    queue = deque()
    queue.append((x,y))
    while move:
        x,y = queue.popleft()
        dir = move.popleft()
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < n and 0 <= ny < m:
            dice = roll(dice,dir)
            print(dice[2])
            if graph[nx][ny] != 0:
                dice[5] = graph[nx][ny]
                graph[nx][ny] = 0
            else:
                graph[nx][ny] = dice[5]

            queue.append((nx,ny))
        else:
            queue.append((x,y))

bfs(x,y)