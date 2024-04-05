from collections import deque

n = int(input())
queue = deque([i for i in range(1, n+1)])

throwable = True
while queue:
    x = queue.popleft()
    if throwable:
        print(x, end=" ")
        throwable = False
    else:
        queue.append(x)
        throwable = True