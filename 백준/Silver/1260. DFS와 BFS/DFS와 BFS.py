from collections import deque

N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
visited2 = [False] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(graph,start,visited):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited2):
    queue = deque()
    queue.append(start)
    visited2[start] = True

    while queue:
        x = queue.popleft()
        print(x, end=" ")
        for i in graph[x]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True

dfs(graph,V,visited)
print()
bfs(graph,V,visited2)