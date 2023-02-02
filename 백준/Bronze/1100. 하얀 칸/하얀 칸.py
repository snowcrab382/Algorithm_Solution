count = 0
for i in range(8):
    b = list(input())
    if i % 2 == 0:
        for x in b[::2]:
            if x == 'F':
                count += 1
    else:
        for y in b[1::2]:
            if y == 'F':
                count += 1
print(count)