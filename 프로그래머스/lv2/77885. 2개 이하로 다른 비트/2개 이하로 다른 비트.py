def solution(numbers):
    result = []
    for i in numbers:
        tmp = bin(i)[2:]
        tmp = list(tmp.zfill(len(tmp)+1))
        for j in range(len(tmp)-1,0,-1):
            if (tmp[j] == '0' and tmp[j-1] == '0') or (tmp[j] == '0' and tmp[j-1] == '1'):
                tmp[j] = '1'
                result.append(int(''.join(tmp),2))
                break
            elif tmp[j] == '1' and tmp[j-1] == '0':
                tmp[j],tmp[j-1] = '0','1'
                result.append(int(''.join(tmp),2))
                break
    return result
