from itertools import permutations 

N,M = map(int,input().split())
a = map(str, range(1,N+1))

perm = list(permutations(a,M))
for i in perm:
    print(" ".join(i))