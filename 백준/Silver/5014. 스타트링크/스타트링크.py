from collections import deque

F,S,G,U,D = map(int,input().split())
visited = [0] * (F+1)

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = 1
    while queue:
        x = queue.popleft()
        if x == G:
            return visited[G]-1
        for X in (x+U,x-D):
            if 1 <= X <= F and not visited[X]:
                visited[X] = visited[x] + 1
                queue.append(X)

    return "use the stairs"

print(bfs(S))