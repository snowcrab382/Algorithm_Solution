a,b,c = map(int,input().split())

def recursion(a,b,c):
    if b == 1:
        return a % c

    val = recursion(a,b//2,c)

    if b % 2 == 0:
        return (val * val) % c
    else:
        return (val * val * a) % c

print(recursion(a,b,c))