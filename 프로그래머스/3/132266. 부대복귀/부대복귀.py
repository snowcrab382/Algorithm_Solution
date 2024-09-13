from collections import deque
import sys

def solution(n, roads, sources, destination):
    answer = []
    result = [-1] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    def bfs(x):
        visited = [0] * (n + 1)
        visited[x] = 1
        q = deque([(x, 0)])
        
        while q:
            node, cnt = q.popleft()
            result[node] = cnt
            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = 1
                    q.append((next_node, cnt + 1))

    bfs(destination)
    for source in sources:
        answer.append(result[source])
            
    return answer

