graph = [list(map(int,input().split())) for _ in range(4)]
result = [[0] * 101 for _ in range(101)]
for a,b,c,d in graph:
    for i in range(a-1,c-1):
        for j in range(b-1,d-1):
            result[i][j] = 1

ans = 0
for i in result:
    for j in i:
        if j == 1:
            ans += 1
print(ans)