graph = [[0] * 101 for _ in range(101)]
n = int(input())

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def curve(x, y, d, g):
    dragon = [(x,y), (x+dx[d], y+dy[d])]
    while g > 0:
        c_x, c_y = dragon[-1]
        search = dragon[-2::-1]
        tmp = []
        for i,j in search:
            r_x, r_y = i - c_x, j - c_y
            r_x, r_y = -r_y + c_x, r_x + c_y
            tmp.append((r_x,r_y))
        for k in tmp:
            dragon.append(k)
        g -= 1
    for a, b in dragon:
        graph[a][b] = 1

def check(x,y):
    if x + 1 > 100 or y + 1 > 100:
        return False
    if graph[x+1][y] == graph[x][y+1] == graph[x+1][y+1] == 1:
        return True
    return False

for _ in range(n):
    x, y, d, g = map(int,input().split())
    curve(x,y,d,g)

ans = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1:
            if check(i,j):
                ans += 1
print(ans)