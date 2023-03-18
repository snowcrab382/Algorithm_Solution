from collections import deque
            
def solution(x, y, n):
    d = [0] * 1000001
    visited = [0] * 1000001
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        visited[start] = 1

        while queue:
            cur = queue.popleft()
            if cur == y:
                return d[y]

            for i in [cur+n,cur*2,cur*3]:
                if 1 <= i <= y+1:
                    if not visited[i]:
                        d[i] = d[cur] + 1
                        visited[i] = 1
                        queue.append(i)
        return -1
                
    return bfs(x)

    

                