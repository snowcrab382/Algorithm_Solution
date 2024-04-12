import sys
input = sys.stdin.readline

num = [0] * 50001
squares = []
for i in range(1, 50001):
    if i % (i**(1/2)) == 0.0:
        num[i] = 1
        squares.append(i)

for i in range(1, 50001):
    if not num[i]:
        tmp = num[i-1] + 1
        for j in squares:
            if j > i:
                break
            tmp = min(tmp, num[j] + num[i-j])
        num[i] = tmp

n = int(input())
print(num[n])