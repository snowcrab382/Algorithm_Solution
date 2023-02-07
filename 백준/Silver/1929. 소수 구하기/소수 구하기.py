m,n = map(int,input().split())
d = [True] * 1000001
d[0],d[1] = False,False

for i in range(3,1001):
    for j in range(2,i):
        if i % j == 0:
            d[i] = False
            continue

for i in range(2,1001):
    if d[i] == False:
        continue
    x = 2
    while x*i < len(d):
        d[x*i] = False
        x += 1

for i in range(m,n+1):
    if d[i] == True:
        print(i)