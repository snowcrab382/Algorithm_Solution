def solution(n, t, m, p):
    result = ''
    i = 0
    while len(result) <= t*m:
        num = ''
        tmp = i
        while True:
            if 10 <= tmp % n <= 15:
                num = chr(tmp % n + 55) + num
            else:
                num = str(tmp % n) + num
            tmp //= n
            if tmp == 0:
                break
        result += num
        i += 1
    return result[p-1:t*m:m]