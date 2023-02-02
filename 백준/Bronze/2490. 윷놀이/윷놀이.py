a = []
for i in range(3):
    b = list(map(int, input().split()))
    if b.count(0) == 1:
        a.append('A')
    elif b.count(0) == 2:
        a.append('B')
    elif b.count(0) == 3:
        a.append('C')
    elif b.count(0) == 4:
        a.append('D')
    elif b.count(0) == 0:
        a.append('E')
for i in a:
    print(i)