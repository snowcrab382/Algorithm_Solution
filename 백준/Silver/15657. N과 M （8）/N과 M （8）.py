n,m = map(int,input().split())
graph = sorted(list(map(int,input().split())))
ans = [0] * 10
visited = [0] * 10

def solve(x):
    if x == m:
        for i in range(m):
            print(graph[ans[i]], end=' ')
        print()
        return
    st = 0
    if x != 0:
        st = ans[x-1]
    for i in range(st,n):
        ans[x] = i
        visited[i] = 1
        solve(x+1)
        visited[i] = 0

solve(0)