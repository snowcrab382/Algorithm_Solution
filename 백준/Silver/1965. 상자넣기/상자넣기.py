n = int(input())
box = list(map(int, input().split()))

dp = [1] * n
for i in range(1, n):
    max_len = 0
    for j in range(i):
        if box[j] < box[i]:
            max_len = max(max_len, dp[j])
    dp[i] = max_len + 1
print(max(dp))