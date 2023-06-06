def bt(day, tmp):
    global ans
    if day == N:
        if ans < tmp:
            ans = tmp
        return
    bt(day+1, tmp)
    if day + a[day][0] <= N:
        bt(day+a[day][0], tmp + a[day][1])

N = int(input())
a = []
for _ in range(N):
    a.append(list(map(int,input().split())))
ans = 0
bt(0, 0)
print(ans)