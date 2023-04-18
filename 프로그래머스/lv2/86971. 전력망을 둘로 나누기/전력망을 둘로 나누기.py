from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for x,y in wires:
        graph[x].append(y)
        graph[y].append(x)
    
    def bfs(start):
        visited = [0 for _ in range(n+1)]
        queue = deque([start])
        visited[start] = 1
        cnt = 1
        while queue:
            x = queue.popleft()
            for i in graph[x]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = 1
                    cnt += 1
        return cnt
    
    result = n
    for x,y in wires:
        graph[x].remove(y)
        graph[y].remove(x)
        
        result = min(result,abs(bfs(x)-bfs(y)))
        
        graph[x].append(y)
        graph[y].append(x)
    return result
        
                
        
