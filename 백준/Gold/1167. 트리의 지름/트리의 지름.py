import sys
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v):
    lines = list(map(int,input().split()))
    node = lines[0]
    for i in range(1, len(lines), 2):
        if lines[i] == -1:
            break
        graph[node].append((lines[i], lines[i+1]))

def dfs(node, distance):
    for next, cost in graph[node]:
        if visited[next] == -1:
            visited[next] = distance + cost
            dfs(next, visited[next])

    return

visited = [-1] * (v+1)
visited[1] = 0
dfs(1, 0)
edge_node, max_len = 0, 0
for i in range(1, v+1):
    if visited[i] > max_len:
        edge_node = i
        max_len = visited[i]

visited = [-1] * (v+1)
visited[edge_node] = 0
dfs(edge_node, 0)
print(max(visited))