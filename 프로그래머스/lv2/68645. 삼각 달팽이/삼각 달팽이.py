def solution(n):
    result = []
    triangle = [[0] * n for _ in range(n)]
    x,y = -1,0
    num = 0
    
    for i in range(n):
        for _ in range(i,n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -=1
                y -=1
            num += 1
            triangle[x][y] = num
    
    for i in range(n):
        for j in triangle[i]:
            if j:
                result.append(j)
    return result