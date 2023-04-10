n = int(input())

for i in range(2,n+1):
    if n == 1:
        break
    while True:
        if n % i == 0:
            n //= i
            print(i)
        else:
            break