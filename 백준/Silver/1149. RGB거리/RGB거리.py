n = int(input())
d = [[0,0,0] for i in range(n+1)]
cost = [[0 for _ in range(n)]]
for _ in range(n):
    cost.append(list(map(int,input().split())))
d[1][0] = cost[1][0] #R
d[1][1] = cost[1][1] #G
d[1][2] = cost[1][2] #B

for i in range(2,n+1):
    for j in range(3):
        if j == 0:
            d[i][0] = min(d[i - 1][1],d[i - 1][2]) + cost[i][0]
        elif j == 1:
            d[i][1] = min(d[i - 1][0], d[i - 1][2]) + cost[i][1]
        else:
            d[i][2] = min(d[i - 1][0], d[i - 1][1]) + cost[i][2]

print(min(d[n]))