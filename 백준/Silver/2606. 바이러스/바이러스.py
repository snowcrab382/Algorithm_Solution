network = [[]]
N = int(input())
for _ in range(N):
    network.append([])

M = int(input())
for _ in range(M):
    a,b = map(int,input().split())
    network[a].append(b)
    network[b].append(a)

visited = [False] * (N+1)
def virus(network,v,visited):
    visited[v] = True
    for i in network[v]:
        if not visited[i]:
            virus(network,i,visited)

virus(network,1,visited)
print(visited.count(True)-1)