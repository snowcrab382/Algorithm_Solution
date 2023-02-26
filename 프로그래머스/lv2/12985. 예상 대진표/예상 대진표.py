def solution(n,a,b):
    cnt = 1
    a -= 1
    b -= 1
    while a//2 != b//2:
        a //= 2
        b //= 2
        cnt += 1
        
    return cnt
