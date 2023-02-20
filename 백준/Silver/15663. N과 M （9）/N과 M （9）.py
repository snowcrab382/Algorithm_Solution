def bt(x):
    if x == m:
        for i in range(m):
            print(result[i], end=' ')
        print()
        return

    tmp = 0
    for i in range(len(graph)):
        if not visited[i] and graph[i] != tmp:
            result[x] = graph[i]
            tmp = result[x]
            visited[i] = 1
            bt(x+1)
            visited[i] = 0

n,m = map(int,input().split())
graph = sorted(list(map(int,input().split())))
visited = [0] * (n+1)
result = [0] * (n+1)

bt(0)