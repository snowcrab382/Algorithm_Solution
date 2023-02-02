N = int(input())
for i in range(N-1):
    print(' '*i + '*'*(2*N-2*i-1))
for j in range(N , 0, -1):
    print(' '*(j-1) + '*'*(2*(N-j)+1))