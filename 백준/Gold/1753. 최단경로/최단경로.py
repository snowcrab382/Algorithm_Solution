import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, tmp = heapq.heappop(queue)

        if distance[tmp] < dist:
            continue

        for i in graph[tmp]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

V, E = map(int,input().split())
k = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((v, w))

dijkstra(k)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])