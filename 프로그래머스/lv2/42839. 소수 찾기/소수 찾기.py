import itertools

def solution(numbers):
    numbers = list(numbers)
    check = set()
    cnt = 0
    for i in range(1,len(numbers)+1):
        for p in itertools.permutations(numbers,i):
            if int(''.join(p)) >= 2:
                check.add(int(''.join(p)))
    
    for j in check:
        sosu = True
        for k in range(2,j):
            if j % k == 0:
                sosu = False
                break
        if sosu:
            cnt += 1
    return cnt