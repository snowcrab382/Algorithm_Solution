def solution(s):
    check = [-1] * 28
    result = []
    for i in range(len(s)):
        tmp = ord(s[i])-97
        if check[tmp] == -1:
            result.append(-1)
            check[tmp] = i
        else:
            result.append(i-check[tmp])
            check[tmp] = i
    return result