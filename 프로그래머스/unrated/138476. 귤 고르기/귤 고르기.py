def solution(k, tangerine):
    check = list(set(tangerine))
    comb = []
    for i in tangerine:
        cnt[i] += 1
    for j in check:
        comb.append(cnt[j])
    comb.sort(reverse = True)
    
    result,tmp = 1,0
    for i in comb:
        tmp += i
        if tmp >= k:
            break
        result += 1
    return result

cnt = [0] * 10000001