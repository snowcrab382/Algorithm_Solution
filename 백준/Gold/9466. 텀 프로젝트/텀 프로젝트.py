import sys
sys.setrecursionlimit(111111)

def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    temp = graph[x]

    if visited[temp]:
        if temp in cycle:
            result += cycle[cycle.index(temp):]
        return
    else:
        dfs(temp)


t = int(input())
for _ in range(t):
    n = int(input())
    graph = [0] + list(map(int,input().split()))
    visited = [True] + [False] * n
    result = []

    for i in range(1,n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n - len(result))