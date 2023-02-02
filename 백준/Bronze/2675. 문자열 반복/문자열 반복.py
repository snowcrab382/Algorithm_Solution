T = int(input())
for i in range(T):
    x, y = input().split()
    for j in range(len(y)):
        print(int(x)*y[j], end='')
    print()