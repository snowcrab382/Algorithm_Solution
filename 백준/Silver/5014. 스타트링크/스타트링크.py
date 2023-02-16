from collections import deque

f,s,g,u,d = map(int,input().split())
floor = [0] * (f+1)

def bfs(x):
    queue = deque()
    queue.append(x)
    floor[x] = 1
    while queue:
        x = queue.popleft()
        if x == g:
            return floor[g]-1
        for i in (x+u,x-d):
            if 1 <= i < f+1 and not floor[i]:
                floor[i] = floor[x] + 1
                queue.append(i)
    return 'use the stairs'

print(bfs(s))