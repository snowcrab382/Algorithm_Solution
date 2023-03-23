def solution(n):
    answer = []
    def hanoi(a,b,n):
        if n == 1:
            answer.append([a,b])
        else:
            hanoi(a,6-a-b,n-1)
            answer.append([a,b])
            hanoi(6-a-b,b,n-1)
        
    hanoi(1,3,n)
    return answer