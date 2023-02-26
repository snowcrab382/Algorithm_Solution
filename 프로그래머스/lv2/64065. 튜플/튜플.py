def solution(s):
    result = []
    answer = s[2:-2].split('},{')
    answer.sort(key = lambda x : len(x))
    for i in answer:
        for j in i.split(','):
            if int(j) not in result:
                result.append(int(j))
                
    return result