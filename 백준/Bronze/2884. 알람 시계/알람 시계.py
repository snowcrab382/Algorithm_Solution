H,M = map(int,input().split())
new_H = H - 1
if new_H < 0:
    new_H = 23
new_M = M + 15
if new_M >= 60:
    new_H += 1
    if new_H == 24:
        new_H = 0
    new_M -= 60
print(new_H, new_M)