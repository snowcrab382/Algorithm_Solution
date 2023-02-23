def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        A[i] = A[i]*B[i]
    
    return sum(A)