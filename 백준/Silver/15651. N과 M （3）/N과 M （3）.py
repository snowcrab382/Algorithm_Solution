n,m = map(int,input().split())
graph = [0] * 10
visited = [0] * 10

def solve(x):
    if x == m:
        for i in range(m):
            print(graph[i], end=' ')
        print()
        return

    for i in range(1,n+1):
        graph[x] = i
        visited[i] = 1
        solve(x+1)
        visited[i] = 0

solve(0)