def solution(s):
    answer = s
    num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(len(num)):
        answer = answer.replace(num[i],str(i))
    return int(answer)
