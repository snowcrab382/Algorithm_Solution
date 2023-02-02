N = int(input())
graph = []
cnt = [0,0]

for _ in range(N):
    graph.append(list(map(int,input().split())))

def check(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[x][y] != graph[i][j]:
                return False
    return True

def solve(x,y,z):
    if check(x,y,z):
        cnt[graph[x][y]] += 1
    else:
        n = z // 2
        for i in range(2):
            for j in range(2):
                solve(x + i * n, y + j * n, n)

solve(0,0,N)
for i in cnt:
    print(i)