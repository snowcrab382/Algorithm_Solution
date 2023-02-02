while True:
    A = list(map(int,input().split()))
    if sum(A) == 0:
        break
    else:
        A.sort()
        if (A[0]**2 + A[1]**2) == A[2]**2:
            print('right')
        else:
            print('wrong')