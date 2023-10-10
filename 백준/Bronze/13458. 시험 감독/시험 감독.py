import math

n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())
result = 0

for i in a:
  if i <= b:
    result += 1
    continue
  else:
    result += math.ceil((i-b) / c) + 1
print(result)