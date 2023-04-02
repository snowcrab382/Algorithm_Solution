def solution(weights):
    result = dict()
    answer = 0
    for i in weights:
        if i not in result.keys():
            result[i] = 1
        else:
            result[i] += 1
            
    for key, val in result.items():
        if val > 1 :
            answer += val * ( val - 1) // 2
        if key*2 in result:
            answer += val * result[key*2]
        if key*3 % 2 == 0 and key*3 // 2 in result:
            answer += val * result[key*3 // 2]
        if key*4 % 3 == 0 and key*4 // 3 in result:
            answer += val * result[key*4 // 3]

    return answer