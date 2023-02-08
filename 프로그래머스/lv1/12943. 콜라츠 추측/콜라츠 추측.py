def solution(num):
    if num == 1:
        return 0
    cnt = 0
    while cnt <= 500:
        if num % 2 == 0:
            num //= 2
        else:
            num = num*3 +1
        cnt += 1
        if num == 1:
            return cnt
    return -1