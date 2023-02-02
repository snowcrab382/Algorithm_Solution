n,m = map(int,input().split())
graph = sorted(list(map(int,input().split())))
ans = [0] * 10

def solve(x):
    if x == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return

    tmp = 0
    for i in range(n):
        if tmp != graph[i]:
            ans[x] = graph[i]
            tmp = ans[x]
            solve(x+1)
solve(0)