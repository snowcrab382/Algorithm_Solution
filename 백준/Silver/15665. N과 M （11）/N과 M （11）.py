def bt(x):
    if x == m:
        for i in range(m):
            print(result[i], end=' ')
        print()
        return

    tmp = 0
    for i in range(len(graph)):
        if graph[i] != tmp:
            result[x] = graph[i]
            tmp = result[x]
            bt(x+1)

n,m = map(int,input().split())
graph = sorted(list(map(int,input().split())))
result = [0] * (n+1)

bt(0)