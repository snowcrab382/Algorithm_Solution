def solution(a):
    answer = 0
    size = len(a)
    check = [0] * size
    tmp = a[0]
    for i in range(1, size):
        if a[i] > tmp:
            check[i] += 1
        else:
            tmp = a[i]
    
    tmp = a[-1]
    for j in range(size-1, -1, -1):
        if a[j] > tmp:
            check[j] += 1
        else:
            tmp = a[j]
    
    for i in check:
        if i <= 1:
            answer += 1
        
    return answer



# 각 숫자마다 양쪽에 더 작은 수가 있는지 확인. 0~1개면 result +1, 2이상이면 불가