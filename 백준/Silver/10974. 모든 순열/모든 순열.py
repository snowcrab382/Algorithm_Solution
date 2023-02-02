import itertools

N = int(input())
N_list = list(i for i in range(1,N+1))

a = list(itertools.permutations(N_list,N))
for x in a:
    for y in x:
        print(y, end=' ')
    print()