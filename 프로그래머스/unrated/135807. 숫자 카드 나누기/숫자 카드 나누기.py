def solution(arrayA, arrayB):
    div_A,div_B = [],[]
    answer = []
    for i in range(1,int((arrayA[0])**0.5)+1):
        if arrayA[0] % i == 0:
            div_A.append(i)
            div_A.append(arrayA[0]//i)
    for j in range(1,int((arrayB[0])**0.5)+1):
        if arrayB[0] % j == 0:
            div_B.append(j)
            div_B.append(arrayB[0]//j)
    
    for x in div_A:
        tmp = True
        for y in arrayA:
            if y % x != 0:
                tmp = False
                break
        if tmp:
            for z in arrayB:
                if z % x == 0:
                    tmp = False
                    break
            if tmp:
                answer.append(x)

    for x in div_B:
        tmp = True
        for y in arrayB:
            if y % x != 0:
                tmp = False
                break
        if tmp:
            for z in arrayA:
                if z % x == 0:
                    tmp = False
                    break
            if tmp:
                answer.append(x)
        
    if len(answer):
        return max(answer)
    else:
        return 0