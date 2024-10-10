from collections import deque, Counter
import sys
INF = sys.maxsize

def solution(n, edge):
    vertex = [[] for _ in range(n+1)]
    for a, b in edge:
        vertex[a].append(b)
        vertex[b].append(a)
    
    q = deque([(0, 1)])
    distance = [INF] * (n+1)
    distance[0] = 0
    distance[1] = 0
    while q:
        cnt, node = q.popleft()
        for next in vertex[node]:
            if distance[next] > cnt + 1:
                distance[next] = cnt + 1
                q.append((distance[next], next))
    answer = Counter(distance)
    return answer[max(distance)]
