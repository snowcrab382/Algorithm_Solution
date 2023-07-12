from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    if b in graph[a]:
        continue
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph,start):
    num = [0] * (n+1)
    visited = [False] * (n+1)
    visited[start] = True
    queue = deque()
    queue.append(start)

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                num[i] = num[x] + 1
                visited[i] = True
                queue.append(i)
    return sum(num)

tmp = 100
result = 0
for i in range(n,0,-1):
    if bfs(graph,i) <= tmp:
        tmp = bfs(graph,i)
        result = i
print(result)