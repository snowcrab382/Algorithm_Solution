n = int(input())
tri = [[]]
tmp = [[]]
for i in range(1,n+1):
    tri.append(list(map(int,input().split())))
    tmp.append([0 for x in range(i)])

if n == 1:
    print(tri[1][0])
    exit(0)
tmp[1][0] = tri[1][0]
tmp[2][0] = tmp[1][0] + tri[2][0]
tmp[2][1] = tmp[1][0] + tri[2][1]

for i in range(3,n+1):
    tmp[i][0] = tmp[i-1][0] + tri[i][0]
    tmp[i][i-1] = tmp[i-1][i-2] + tri[i][i-1]
    for j in range(1,i-1):
        tmp[i][j] = max(tmp[i-1][j],tmp[i-1][j-1]) + tri[i][j]
print(max(tmp[n]))