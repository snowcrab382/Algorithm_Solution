n, m = map(int,input().split())
graph = [list(map(int, input())) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and graph[i][j] == 1:
            graph[i][j] += min(graph[i][j-1], graph[i-1][j], graph[i-1][j-1])
        result = max(result, graph[i][j])
print(result**2)