def bt(x):
    global cnt
    if sum(result) == s and len(result) > 0:
        cnt += 1
        

    for i in range(x,n):
        result.append(graph[i])
        bt(i+1)
        result.pop()

n,s = map(int,input().split())
graph = list(map(int,input().split()))
result = []
cnt = 0

bt(0)
print(cnt)