def solution(cards):
    result = []
    answer = [0]
    visited = [0] * (len(cards)+1)
    for i in cards:
        answer.append(i)
    
    for i in range(1,len(answer)):
        if not visited[i]:
            tmp = i
            tmp_cnt = 1
            while True:
                visited[tmp] = 1
                if answer[tmp] == i:
                    break
                tmp = answer[tmp]
                tmp_cnt += 1
            result.append(tmp_cnt)
    if len(result) == 1:
        return 0
    else:
        result.sort(reverse = True)
        return result[0]*result[1]

