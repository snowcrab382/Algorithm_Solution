N = list(map(int, input()))

if 0 not in N or sum(N) % 3 != 0:
    print('-1')
else:
    N.sort(reverse = True)
    for i in N:
        print(i, end='')