from collections import deque

n = int(input())
m = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

plan = list(map(int,input().split()))
for i in range(len(plan)):
    plan[i] -= 1

start_node = plan[0]
plan = set(plan)
cities = {start_node}
visited = [0] * n
visited[start_node] = 1
queue = deque([start_node])

while queue:
    x = queue.popleft()
    for i in range(n):
        if graph[x][i] and not visited[i]:
            cities.add(i)
            queue.append(i)
            visited[i] = 1

if plan.issubset(cities):
    print("YES")
else:
    print("NO")