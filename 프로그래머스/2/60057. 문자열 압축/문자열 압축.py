import sys
MAX = sys.maxsize

def solution(s):
    answer = MAX
    s_len = len(s)
    for i in range(1, s_len + 1):
        comp = ''
        cnt = 1
        tmp = s[0:i]
        for j in range(i, s_len, i):
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                if cnt != 1:
                    comp += str(cnt)
                comp += tmp

                tmp = s[j:j+i]
                cnt = 1
        if cnt != 1:
            comp += str(cnt)
        comp += tmp

        answer = min(answer, len(comp))
    return answer