import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int,input().split())
parent = [i for i in range(n+1)]

def union(a,b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

for _ in range(m):
    o, a, b = map(int,input().split())
    if not o:
        union(a,b)
    if o:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")