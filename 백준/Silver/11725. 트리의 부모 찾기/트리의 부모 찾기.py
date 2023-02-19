import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    for i in graph[x]:
        if not result[i]:
            result[i] = x
            dfs(i)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

result = [0] * (n+1)
result[1] = True

dfs(1)
for i in result[2:]:
    print(i)