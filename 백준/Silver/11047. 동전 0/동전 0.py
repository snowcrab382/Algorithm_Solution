N, K = map(int,input().split())
coin = []
result = 0

for _ in range(N):
    coin.append(int(input()))

for i in sorted(coin, reverse = True):
    if K // i != 0:
        result += K // i
        K = K % i
print(result)