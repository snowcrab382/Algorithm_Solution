R,C,M = map(int,input().split())
graph = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    graph[r-1][c-1].append([s,d,z])

dx = [0,-1,1,0,0]
dy = [0,0,0,1,-1]

def catch(y):
    size = 0
    for i in range(R):
        if graph[i][y]:
            size += graph[i][y][0][2]
            graph[i][y] = []
            break
    return size

def move(graph):
    temp = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j]:
                s,d,z = graph[i][j][0]
                nx,ny = i,j
                dist = s
                while dist:
                    nx += dx[d]
                    ny += dy[d]
                    if 0 <= nx < R and 0 <= ny < C:
                        dist -= 1
                    else:
                        nx -= dx[d]
                        ny -= dy[d]
                        if d % 2 != 0:
                            d += 1
                        else:
                            d -= 1
                temp[nx][ny].append([s,d,z])

    for i in range(R):
        for j in range(C):
            if len(temp[i][j]) > 1:
                temp[i][j].sort(key = lambda x : -x[2])
    return temp


result = 0
for i in range(C):
    result += catch(i)
    graph = move(graph)
print(result)