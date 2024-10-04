value = 2000000000
n = int(input())
x, y = 0, 0
l = 0
r = n - 1

li = list(map(int, input().split()))

while l < r:
    curr = li[l] + li[r]

    if abs(curr) <= value:
        value = abs(curr)
        x = li[l]
        y = li[r]

    if curr <= 0:
        l += 1
    else:
        r -= 1
print(x, y)