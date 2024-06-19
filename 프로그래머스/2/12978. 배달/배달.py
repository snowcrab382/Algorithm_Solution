import heapq
import sys
MAX = sys.maxsize

def solution(N, road, K):
    answer = 1
    distance = [MAX] * (N+1)
    
    roads = [[] for _ in range(N+1)]
    for a, b, c in road:
        roads[a].append((c,b))
        roads[b].append((c,a))
    
    pq = [(0,1)]
    while pq:
        tmp_cost, tmp_node = heapq.heappop(pq)
        for cost, node in roads[tmp_node]:
            if tmp_cost + cost <= distance[node]:
                distance[node] = tmp_cost + cost
                heapq.heappush(pq, (distance[node], node))
                
    for i in distance[2:]:
        if i <= K:
            answer += 1

    return answer

