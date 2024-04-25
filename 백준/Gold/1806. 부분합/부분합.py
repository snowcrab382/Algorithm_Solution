import sys
input = sys.stdin.readline

n, s = map(int,input().split())
arr = list(map(int,input().split()))

left, right, sum = 0, 0, 0
result = n+1

while True:
    if sum >= s:
        result = min(result, right-left)
        sum -= arr[left]
        left += 1
    elif right == n:
        break
    else:
        sum += arr[right]
        right += 1

if result == n+1:
    print(0)
else:
    print(result)