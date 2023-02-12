def solution(s):
    result = []
    num = dict(zero=0, one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9)
    temp = ''
    for i in range(len(s)):
        if s[i].isdigit():
            result.append(s[i])
        else:
            temp += s[i]
            if temp in num:
                result.append(str(num[temp]))
                temp = ''
    answer = int(''.join(result))
    return answer
