a = []
for i in range(5):
    b = list(map(int,input().split()))
    a.append(sum(b))
print(a.index(max(a))+1, max(a))