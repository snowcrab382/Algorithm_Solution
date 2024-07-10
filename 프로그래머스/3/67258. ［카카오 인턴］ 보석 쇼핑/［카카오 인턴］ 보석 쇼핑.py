def solution(gems):
    size = len(gems)
    answer = [0, size-1]
    distinct = set(gems)
    l, r = 0, 0
    dic = {gems[0]: 1}
    
    while l < size and r < size:
        if len(dic) < len(distinct):
            r += 1
            if r == size:
                break
            dic[gems[r]] = dic.get(gems[r], 0) + 1
        else:
            if r - l < answer[1] - answer[0]:
                answer = [l, r]
            if dic[gems[l]] == 1:
                del dic[gems[l]]
            else:
                dic[gems[l]] -= 1
            l += 1
    
    answer[0] += 1
    answer[1] += 1
    return answer