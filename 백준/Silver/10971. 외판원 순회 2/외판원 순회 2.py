n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
count = 10000000

def bt(start,next,value,visited):
    global count

    if len(visited) == n:
        if a[start][next] != 0:
            count = min(count,value+a[start][next])
        return
    for i in range(n):
        if a[i][next] != 0 and i not in visited and value < count:
            visited.append(i)
            bt(start,i,value+a[i][next],visited)
            visited.pop()

for i in range(n):
    bt(i,i,0,[i])

print(count)