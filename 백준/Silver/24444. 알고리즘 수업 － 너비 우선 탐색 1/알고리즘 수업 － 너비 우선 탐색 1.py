from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

def bfs(r):
    cnt = 1
    visited[r] = cnt
    queue = deque()
    queue.append(r)

    while queue:
        x = queue.popleft()
        for i in sorted(graph[x]):
            if not visited[i]:
                cnt += 1
                visited[i] = cnt
                queue.append(i)

for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(r)

for i in range(1, n+1):
    print(visited[i])