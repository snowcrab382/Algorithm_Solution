T = int(input())
for i in range(T):
    a = list(input().split(' '))
    for j in a:
        print(j[::-1], end=' ')