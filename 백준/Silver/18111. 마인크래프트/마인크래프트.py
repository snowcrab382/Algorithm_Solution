import sys
input = sys.stdin.readline

n, m, b = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(n)]
result = sys.maxsize
idx = 0
for i in range(257):
    get, use = 0, 0
    for j in range(n):
        for k in range(m):
            if ground[j][k] > i:
                get += ground[j][k] - i
            else:
                use += i - ground[j][k]
    if get + b >= use:
        if get * 2 + use <= result:
            result = get * 2 + use
            idx = i
print(result, idx)