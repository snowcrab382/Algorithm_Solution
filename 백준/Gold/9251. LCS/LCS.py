a = input()
b = input()
lenA, lenB = len(a), len(b)
cache = [0] * lenB

for i in range(lenA):
    cnt = 0
    for j in range(lenB):
        if cnt < cache[j]:
            cnt = cache[j]
        elif a[i] == b[j]:
            cache[j] = cnt + 1
print(max(cache))