n = int(input())
arr = list(map(int,input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
max_len = max(dp)
print(max_len)

result = []
for i in range(n-1,-1,-1):
    if dp[i] == max_len:
        result.append(arr[i])
        max_len -= 1
    if not max_len:
        break
result.reverse()
print(*result)