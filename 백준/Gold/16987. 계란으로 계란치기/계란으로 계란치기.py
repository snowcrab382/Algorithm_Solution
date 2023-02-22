def bt(x):
    global max_cnt
    cnt = 0
    if x == n:
        for i in graph:
            if i[0] <= 0:
                cnt += 1
        max_cnt = max(max_cnt,cnt)
        return

    if graph[x][0] <= 0:
        bt(x+1)
    else:
        flag = False
        for i in range(n):
            if graph[i][0] <= 0 or x == i:
                continue
            graph[x][0] -= graph[i][1]
            graph[i][0] -= graph[x][1]
            flag = True
            bt(x+1)
            graph[x][0] += graph[i][1]
            graph[i][0] += graph[x][1]
        if not flag:
            bt(x+1)

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
max_cnt = 0
bt(0)
print(max_cnt)