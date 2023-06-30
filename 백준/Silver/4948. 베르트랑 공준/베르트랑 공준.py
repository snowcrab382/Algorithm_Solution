num = [1] * 300000
for i in range(1,len(num)):
    if i == 1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            num[i] = 0
            break

while True:
    n = int(input())
    if not n:
        break
    sosu = 0
    for i in range(n+1,n*2+1):
        sosu += num[i]
    print(sosu)