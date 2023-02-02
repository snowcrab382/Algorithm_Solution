n = int(input())
a = [0,1]
if n == 0:
    print('0')
elif n == 1:
    print('1')
else:
    for i in range(n-1):
        a.append(a[-1] + a[-2])
    print(a[-1])