import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start):
    global cnt
    visited[start] = cnt
    graph[start].sort(reverse=True)
    for i in graph[start]:
        if not visited[i]:
            cnt += 1
            dfs(i)
dfs(r)

for i in range(1, n+1):
    print(visited[i])