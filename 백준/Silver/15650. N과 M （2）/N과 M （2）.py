n,m = map(int,input().split())
graph = [0] * 10
visited = [0] * 10

def solve(x):
    if x == m:
        for i in range(m):
            print(graph[i], end=' ')
        print()
        return
    start = 1
    if x != 0:
        start = graph[x-1] + 1
    for i in range(start,n+1):
        if not visited[i]:
            graph[x] = i
            visited[i] = 1
            solve(x+1)
            visited[i] = 0

solve(0)