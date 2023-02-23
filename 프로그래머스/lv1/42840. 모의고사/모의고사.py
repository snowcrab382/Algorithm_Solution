def solution(answers):
    a = [1,2,3,4,5]*2000
    b = [2,1,2,3,2,4,2,5]*1250
    c = [3,3,1,1,2,2,4,4,5,5]*1000
    
    cnt_a,cnt_b,cnt_c = 0,0,0
    result = []
    for i in range(len(answers)):
        if answers[i] == a[i]:
            cnt_a += 1
        if answers[i] == b[i]:
            cnt_b += 1
        if answers[i] == c[i]:
            cnt_c += 1
    max_cnt = max(cnt_a,cnt_b,cnt_c)
    if cnt_a == max_cnt:
        result.append(1)
    if cnt_b == max_cnt:
        result.append(2)
    if cnt_c == max_cnt:
        result.append(3)
    
    return result