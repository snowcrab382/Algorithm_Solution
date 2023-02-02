a = []
for i in range(28):
    a.append(int(input()))
for j in range(1,31):
    if j not in a:
        print(j)