E,S,M = map(int,input().split())
count = 0
i,j,k = 0,0,0
while True:
    count += 1
    i += 1
    j += 1
    k += 1
    if i > 15:
        i = 1
    if j > 28:
        j = 1
    if k > 19:
        k = 1
    if E == i and S == j and M == k:
        break
print(count)