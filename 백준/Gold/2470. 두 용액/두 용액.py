n = int(input())
arr = sorted(list(map(int,input().split())))
left, right = 0, n - 1

result = abs(arr[left] + arr[right])
answer = [arr[left], arr[right]]

while left < right:
    left_val, right_val = arr[left], arr[right]

    tmp = left_val + right_val

    if abs(tmp) < result:
        result = abs(tmp)
        answer = [left_val, right_val]
        if result == 0:
            break
    if tmp < 0:
        left += 1
    else:
        right -= 1
print(*answer)