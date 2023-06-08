n = int(input())
a = list(map(int,input().split()))
m = int(input())
start,end = 0,max(a)

while start <= end:
    mid = (start+end) // 2
    tot = 0
    for i in a:
        if i <= mid:
            tot += i
        else:
            tot += mid
    if tot <= m:
        start = mid+1
    else:
        end = mid-1
print(end)