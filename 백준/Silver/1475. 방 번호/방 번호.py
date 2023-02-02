a = list(map(int, str(input())))
for i in range(len(a)):
    if a[i] == 6:
        a[i] = 9
b = []
for i in range(0,9):
    b.append(a.count(i))
if max(b) >= a.count(9):
    print(max(b))
else:
    print(a.count(9)//2 + a.count(9)%2)