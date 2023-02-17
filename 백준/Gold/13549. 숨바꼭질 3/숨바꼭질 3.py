from collections import deque

def bfs(x):
    queue = deque()
    queue.append(x)
    graph[x] = 1
    while queue:
        x = queue.popleft()
        if x == k:
            return graph[k]-1

        for i in (2*x,x+1,x-1):
            if 0 <= i <= 100000 and not graph[i]:
                if i == 2*x:
                    graph[i] = graph[x]
                    queue.appendleft(i)
                else:
                    graph[i] = graph[x] + 1
                    queue.append(i)

    return graph[k]


n,k = map(int,input().split())
graph = [0] * 100001
print(bfs(n))