M = int(input())             
N = int(input())
a = []
for i in range(M,N+1):
    if i**0.5 == int(i ** 0.5):
        a.append(i)
if len(a) == 0:
    print('-1')
else:
    print(sum(a))
    print(min(a))