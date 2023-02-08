def solution(a, b):
    d = [i-10000000 for i in range(20000001)]
    if a > b:
        return sum(d[b+10000000:a+10000001])
    return sum(d[a+10000000:b+10000001])