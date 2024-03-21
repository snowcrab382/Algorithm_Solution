def solution(m, n, puddles):
    graph = [[0] * m for _ in range(n)]

    graph[0][0] = 1
    for x, y in puddles:
        graph[y - 1][x - 1] = -1
        
    return dfs(m-1, n-1, graph)
    
def dfs(x, y, graph):
    if x < 0 or y < 0 or graph[y][x] == -1:
        return 0
        
    if graph[y][x] == 0:
        graph[y][x] = dfs(x-1, y, graph) + dfs(x, y-1, graph)

    return graph[y][x] % 1000000007