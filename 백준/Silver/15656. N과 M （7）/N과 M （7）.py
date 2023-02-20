def bt(x):
    if x == m:
        for i in range(m):
            print(result[i], end=' ')
        print()
        return

    for i in graph:
            result[x] = i
            bt(x+1)

n,m= map(int,input().split())
graph = sorted(list(map(int,input().split())))
result = [0] * (n+1)
bt(0)