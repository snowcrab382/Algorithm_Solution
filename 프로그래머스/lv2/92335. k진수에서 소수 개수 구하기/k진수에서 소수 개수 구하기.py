from collections import deque

def solution(n, k):
    cnt = 0
    tmp = ''
    while n != 0:
        tmp = str(n%k) + tmp
        n //= k
    tmp = tmp.split('0')

    for i in tmp:
        sosu = True
        if len(i) == 0 or int(i) < 2:
            continue
        else:
            for x in range(2,int(int(i)**0.5)+1):
                if int(i) % x == 0:
                    sosu = False
                    break
        
        if sosu:
            cnt += 1
    return cnt