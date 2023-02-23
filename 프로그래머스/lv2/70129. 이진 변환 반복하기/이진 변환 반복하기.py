def solution(s):
    answer = [0,0]
    while s != '1':
        for i in s:
            if i == '0':
                answer[1] += 1
        s = s.replace('0','')
        s = str(bin(len(s)))[2:]  
        answer[0] += 1
    return answer