c = 0
hap = []
for i in range(4):
    a,b = map(int,input().split())
    c = c-a+b
    hap.append(c)
print(max(hap))