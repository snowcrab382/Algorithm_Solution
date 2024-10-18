import sys
MAX = sys.maxsize

def solution(n, times):
    s, e = 0, MAX
    while s <= e:
        m = (s + e) // 2
        
        tmp = 0
        for time in times:
            tmp += m // time
        
        if tmp >= n:
            e = m - 1
        else:
            s = m + 1
        
    
    return s