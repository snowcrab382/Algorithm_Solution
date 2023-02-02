import sys
input = sys.stdin.readline

def check(x,y,N):
    for i in range(x,x+N):
        for j in range(y,y+N):
            if graph[i][j] != graph[x][y]:
                return False
    return True

def search(x,y,z):
    if check(x,y,z):
        count[graph[x][y]+1] += 1
    else:
        n = z//3
        for i in range(3):
            for j in range(3):
                search(x + i*n, y+ j*n,n)


count = [0,0,0]
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

search(0,0,N)
for i in count:
    print(i)