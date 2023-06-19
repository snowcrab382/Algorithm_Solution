import itertools

n = int(input())
a = list(map(int,input().split()))
perms = itertools.permutations(a,n)
result = []

for perm in perms:
    tmp = 0
    for i in range(n-1):
        tmp += abs(perm[i] - perm[i+1])
    result.append(tmp)
print(max(result))