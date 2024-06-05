from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
inDegree = [0] * (n+1)
queue = deque()
answer = []

for _ in range(m):
    a, b = map(int,input().split())
    inDegree[b] += 1
    graph[a].append(b)

for i in range(1, n+1):
    if not inDegree[i]:
        queue.append(i)

while queue:
    tmp = queue.popleft()
    if not inDegree[tmp]:
        answer.append(tmp)

    for i in graph[tmp]:
        inDegree[i] -= 1
        if not inDegree[i]:
            queue.append(i)
print(*answer)