n = int(input())
a = [0] * 10000
for i in range(n):
    a[i] = int(input())

dp = [0] * 10000
dp[0] = a[0]
dp[1] = a[0]+a[1]
dp[2] = max(a[2]+a[0], a[2]+a[1], dp[1])
for i in range(3,n):
    dp[i] = max(a[i]+dp[i-2], a[i]+a[i-1]+dp[i-3], dp[i-1])

print(max(dp))