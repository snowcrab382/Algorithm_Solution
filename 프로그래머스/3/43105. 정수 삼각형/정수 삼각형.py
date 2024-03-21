def solution(triangle):
    n = len(triangle)
    
    if n == 1:
        return triangle[0][0]
    else:
        for i in range(1, n):
            for j in range(i + 1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])


        answer = max(triangle[-1])    
        return answer

# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5


# 같은 ind or ind+1 로 이동 가능
# dp로 저장
# 맨 아래까지 갔을때 최댓값 반환

