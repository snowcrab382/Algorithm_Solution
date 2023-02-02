n,m = map(int,input().split())
graph = sorted(list(map(int,input().split())))
ans = [0] * 10
visited = [0] * 10

def solve(x):
    if x == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return
    tmp = 0
    for i in range(n):
        if not visited[i] and tmp != graph[i]:
            ans[x] = graph[i]
            visited[i] = 1
            tmp = ans[x]
            solve(x+1)
            visited[i] = 0

solve(0)