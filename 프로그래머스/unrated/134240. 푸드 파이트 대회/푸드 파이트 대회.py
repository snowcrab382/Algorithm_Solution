def solution(food):
    result = ''
    for i in range(1,len(food)):
        for j in range(food[i]//2):
            result += str(i)
    result = result + '0' + result[::-1]
    return result