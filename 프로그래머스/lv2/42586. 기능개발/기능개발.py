import math

def solution(progresses, speeds):
    n = len(progresses)
    a = [0] * n
    for i in range(n):
        a[i] = math.ceil((100-progresses[i])/speeds[i])
    
    result = []
    tmp, cnt = a[0],1
    for i in range(1,n):
        if tmp >= a[i]:
            cnt += 1
        else:
            result.append(cnt)
            tmp = a[i]
            cnt = 1
        if i == n-1:
            result.append(cnt)
    
    return result