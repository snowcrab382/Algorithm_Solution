import sys
input = sys.stdin.readline

def star(n):
    if n == 3:
        return ['***','* *','***']

    temp = star(n//3)
    result = []

    for i in temp:
        result.append(i*3)
    for i in temp:
        result.append(i+' '*(n//3)+i)
    for i in temp:
        result.append(i*3)
    return result

n = int(input())
print('\n'.join(star(n)))