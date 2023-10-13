from collections import deque

n = int(input())
graph = []
pos = []
for i in range(n):
    row = list(map(int,input().split()))
    graph.append(row)
    for j in range(n):
        if row[j] == 9:
            pos.append(i)
            pos.append(j)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    visited = [[0] * n for _ in range(n)]
    queue = deque()
    queue.append((x,y))
    cand = []
    visited[x][y] = 1
    while queue:
        i, j = queue.popleft()
        for idx in range(4):
            ii, jj = i + dx[idx], j + dy[idx]
            if 0 <= ii and ii < n and 0 <= jj and jj < n and visited[ii][jj] == 0:
                # 5. 간선은 상하 좌우지만 조건에 따라서 움직이기 때문에 조건을 상세하여야한다.
                if graph[x][y] > graph[ii][jj] and graph[ii][jj] != 0:
                    visited[ii][jj] = visited[i][j] + 1
                    cand.append((visited[ii][jj] - 1, ii, jj))
                elif graph[x][y] == graph[ii][jj]:
                    visited[ii][jj] = visited[i][j] + 1
                    queue.append([ii, jj])
                elif graph[ii][jj] == 0:
                    visited[ii][jj] = visited[i][j] + 1
                    queue.append([ii, jj])
    return sorted(cand, key = lambda x : (x[0], x[1], x[2]))

i,j = pos
size = [2,0]
cnt = 0
while True:
    graph[i][j] = size[0]
    cand = deque(bfs(i,j))
    if not cand:
        break
    dist,xx,yy = cand.popleft()
    cnt += dist
    size[1] += 1

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    graph[i][j] = 0
    i, j = xx, yy
print(cnt)