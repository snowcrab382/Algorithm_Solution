def solution(s):
    length = len(s)
    answer = 0
    for i in range(1, length+1):
        for j in range(0, length):
            if j+i > length:
                continue
            tmp = s[j:j+i]
            if tmp == tmp[::-1]:
                answer = i

    return answer
