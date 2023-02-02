N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
cute = a.count(1)
notcute = a.count(0)
if cute > notcute:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')