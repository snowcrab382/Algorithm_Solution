import sys
sys.setrecursionlimit(10**6)

def solution(edges):
    def check(start, tmp):
        if not graph[tmp]:
            answer[2] += 1
            return
        
        if len(graph[tmp]) == 2:
            answer[3] += 1
            return
        
        for node in graph[tmp]:
            if start == node:
                answer [1] += 1
                return
            
            check(start, node)
            
        
    answer = [0,0,0,0]
    graph = [[] for _ in range(1000001)]
    visited = [0] * 1000001
    
    for a,b in edges:
        graph[a].append(b)
        visited[b] = 1
    
    max_cnt = 0
    for i in range(len(graph)):
        if len(graph[i]) > max_cnt and not visited[i]:
            answer[0] = i
            max_cnt = len(graph[i])

    for i in graph[answer[0]]:
        check(i, i)
            
    return answer

