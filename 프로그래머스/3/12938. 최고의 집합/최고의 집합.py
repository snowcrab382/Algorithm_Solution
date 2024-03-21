def solution(n, s):
    if n > s:
        return [-1]
    
    q = s // n
    r = s % n
    result = [q for _ in range(n)]
    
    for i in range(1, r + 1):
        result[-i] += 1
    
    return result