a = set()
i = 1
j = 0
while True:
    j = i + sum(list(map(int,str(i))))
    if i < 10000:
        a.add(j)
    else:
        break
    i += 1
for k in range(1,10001):
    if k not in a:
        print(k)