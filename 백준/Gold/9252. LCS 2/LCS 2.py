a, b = [''] + list(input()), [''] + list(input())
lenA, lenB = len(a), len(b)
dp = [[''] * lenA for _ in range(lenB)]

for i in range(1, lenB):
    for j in range(1, lenA):
        if a[j] == b[i]:
            dp[i][j] = dp[i-1][j-1] + a[j]
        else:
            if len(dp[i][j-1]) > len(dp[i-1][j]):
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]
answer = len(dp[-1][-1])
print(answer)
if answer:
    print(dp[-1][-1])