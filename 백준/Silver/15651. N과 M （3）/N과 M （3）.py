def bt(k):
    global start
    if k == m:
        for i in range(m):
            print(graph[i], end=' ')
        print()
        return

    for i in range(1,n+1):
        graph[k] = i
        bt(k+1)

n,m = map(int,input().split())
graph = [0] * (n+1)

bt(0)