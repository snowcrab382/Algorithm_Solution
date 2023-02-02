a= []
for i in range(7):
    b = int(input())
    if b % 2 != 0:
        a.append(b)
if len(a) == 0:
    print(-1)
else:
    print(sum(a))
    print(min(a))