from collections import deque
import sys

def bfs(x):
    global cnt
    queue = deque()
    queue.append(x)
    visited[x] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    cnt += 1

input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
print(cnt)