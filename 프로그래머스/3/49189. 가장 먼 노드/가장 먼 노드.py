from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range (n + 1)]
    distance = [-1] * (n+1)
    for i,j in edge:
        graph[i].append(j)
        graph[j].append(i)
    
    q = deque([1])
    distance[1] = 0
    while q:
        x = q.popleft()
        
        for i in graph[x]:
            if distance[i] == -1:
                q.append(i)
                distance[i] = distance[x] + 1
    for j in distance:
        if j == max(distance):
            answer += 1

    
    return answer