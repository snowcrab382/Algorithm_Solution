import sys
MAX_SIZE = sys.maxsize

n = int(input())
maze = list(map(int, input().split()))
dp = [[MAX_SIZE, i] for i in maze]

dp[0][0] = 0
for i in range(n):
    jump = dp[i][1]
    for j in range(i + 1, i + 1 + jump):
        if j == n:
            break
        dp[j][0] = min(dp[j][0], dp[i][0] + 1)

print(-1) if dp[-1][0] == MAX_SIZE else print(dp[-1][0])
