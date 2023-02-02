a = []
b = []
a_coor = 0
b_coor = 0
for i in range(3):
    A,B = map(int,input().split())
    a.append(A)
    b.append(B)
for x in a:
    if a.count(x) == 1:
        a_coor = x
for y in b:
    if b.count(y) == 1:
        b_coor = y
print(a_coor, b_coor)