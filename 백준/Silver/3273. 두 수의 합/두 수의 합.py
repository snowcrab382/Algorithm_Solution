n = int(input())
arr = sorted(list(map(int,input().split())))
x = int(input())

cnt = 0
left,right = 0,n-1
while left < right:
    temp = arr[left] + arr[right]
    if temp == x:
        cnt += 1
        left += 1
    elif temp > x:
        right -= 1
    else:
        left += 1
print(cnt)