from math import gcd

def solution(arrayA, arrayB):
    def get_gcd(arr):
        g = arr[0]
        for i in range(1,len(arr)):
            g = gcd(g,arr[i])
        return g
    
    div_A,div_B = get_gcd(arrayA),get_gcd(arrayB)
    answer = []

    for x in arrayB:
        tmp = True
        if x % div_A == 0:
            tmp = False
            break
    if tmp:
        answer.append(div_A)
        
    for y in arrayA:
        tmp = True
        if not y % div_B:
            tmp = False
            break
    if tmp:
        answer.append(div_B)
        
    if len(answer):
        return max(answer)
    else:
        return 0