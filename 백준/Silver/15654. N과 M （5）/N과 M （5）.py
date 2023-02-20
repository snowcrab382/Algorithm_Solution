def bt(x):
    if x == m:
        for i in range(m):
            print(result[i], end=' ')
        print()
        return

    for i in graph:
        if not visited[i]:
            result[x] = i
            visited[i] = 1
            bt(x+1)
            visited[i] = 0

n,m= map(int,input().split())
graph = sorted(list(map(int,input().split())))
visited = [0] * 10001
result = [0] * (n+1)

bt(0)