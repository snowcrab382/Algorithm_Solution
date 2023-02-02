A = list(map(int,input().split()))
B = [1,1,2,2,2,8]
for i in range(len(A)):
    if B[i] - A[i] != 0:
        print(B[i]-A[i], end = ' ')
    else:
        print('0', end= ' ')