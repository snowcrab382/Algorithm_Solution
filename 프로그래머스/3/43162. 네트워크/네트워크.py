from collections import deque

def solution(n, computers):
    visited = [0] * n
    answer = 0
    
    def dfs(start):
        q = deque()
        q.append(start)
        visited[start] = 1
        while q:
            x = q.popleft()
            for i in range(n):
                if computers[x][i] == 1 and not visited[i]:
                    q.append(i)
                    visited[i] = 1
                

    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            
    return answer