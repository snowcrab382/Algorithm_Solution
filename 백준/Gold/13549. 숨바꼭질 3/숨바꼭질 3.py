import sys
import heapq
input = sys.stdin.readline

N,K = map(int,input().split())
INF = int(1e9)

def dijkstra(N,K):
    dist = [INF]*(100001)
    dist[N] =0 
    q = []
    heapq.heappush(q,(0,N))
    while q:
        w,n = heapq.heappop(q)
        for nx in [(n+1,1),(n-1,1),(n*2,0)]:
            if 0<=nx[0]<100001 and dist[nx[0]] > w + nx[1]:
                dist[nx[0]] = w + nx[1]
                heapq.heappush(q,(dist[nx[0]],nx[0]))
    print(dist[K])
    
dijkstra(N,K)