n,m = map(int,input().split())
graph = sorted(list(map(int,input().split())))
ans = [0] * 10

def solve(x,st):
    if x == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return

    tmp = 0
    for i in range(st,n):
        if graph[i] != tmp:
            ans[x] = graph[i]
            tmp = ans[x]
            solve(x+1,i)

solve(0,0)