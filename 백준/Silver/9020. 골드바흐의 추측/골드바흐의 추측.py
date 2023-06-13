n = int(input())

def is_prime(x):
    if x == 1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


for _ in range(n):
    num = int(input())
    up,down = num//2,num//2
    while down > 0:
        if is_prime(up) and is_prime(down):
            print(down,up)
            break
        else:
            up += 1
            down -= 1