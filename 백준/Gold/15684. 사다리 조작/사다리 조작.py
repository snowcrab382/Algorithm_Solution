import sys
input = sys.stdin.readline

n, m, h = map(int,input().split())
graph = [[0] * n for _ in range(h)]
for i in range(m):
    x, y = map(int,input().split())
    graph[x-1][y-1] = 1

def check():
    for i in range(n):
        start = i
        for j in range(h):
            if graph[j][start] == 1:
                start += 1
            elif start > 0 and graph[j][start-1] == 1:
                start -= 1
        if i != start:
            return False
    return True

def backtracking(cnt, x, y):
    global answer
    if answer <= cnt:
        return

    if check():
        answer = min(answer, cnt)
        return

    if cnt == 3:
        return

    for i in range(x, h):
        for j in range(n-1):
            if graph[i][j] == 0:
                graph[i][j] = 1
                backtracking(cnt+1, i, j + 2)
                graph[i][j] = 0

answer = 4
backtracking(0, 0, 0)
if answer > 3:
    print(-1)
else:
    print(answer)