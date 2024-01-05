n, m = map(int,input().split())
num = list(map(int,input().split()))
sum = 0
remainder = [0] * m

for i in range(n):
    sum += num[i]
    remainder[sum % m] += 1

result = remainder[0]

for i in remainder:
    result += i * (i-1) // 2

print(result)