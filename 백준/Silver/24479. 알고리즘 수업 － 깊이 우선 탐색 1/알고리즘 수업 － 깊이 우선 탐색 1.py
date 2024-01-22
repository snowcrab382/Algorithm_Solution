import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m, r = map(int,input().split())
graph = [[] for _ in range (n+1)]
visited = [0] * (n+1)
cnt = 1

def dfs(r):
    global cnt
    visited[r] = cnt
    graph[r].sort()
    for i in graph[r]:
        if not visited[i]:
            cnt += 1
            dfs(i)

for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(r)
for i in range(1, n+1):
    print(visited[i])