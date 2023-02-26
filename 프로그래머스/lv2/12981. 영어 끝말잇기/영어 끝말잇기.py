def solution(n, words):
    num,cnt = 0,1
    check = []
    for i in words:
        num += 1
        if num == n+1:
            num = 1
            cnt += 1
        if len(check) != 0 and (check[-1][-1] != i[0] or i in check):
            return [num,cnt]
        else:
            check.append(i)
    
    return [0,0]