a = list(input())

while True:
    if len(a) < 10:
        break
    for i in a[:10]:
        print(i, end='')
    del a[:10]
    print()
for j in a:
    print(j, end='')