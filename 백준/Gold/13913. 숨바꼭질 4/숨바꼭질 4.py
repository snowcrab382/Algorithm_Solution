from collections import deque

n, k = map(int, input().split())
graph = [-1] * 100001
graph[n] = n
queue = deque([n])
answer = []
while queue:
    x = queue.popleft()

    if x == k:
        while x != n:
            answer.append(x)
            x = graph[x]
        answer.append(n)
        print(len(answer)-1)
        print(*answer[::-1])
        exit(0)

    for nx in (x-1, x+1, x*2):
        if 0 <= nx < 100001 and graph[nx] == -1:
            graph[nx] = x
            queue.append(nx)