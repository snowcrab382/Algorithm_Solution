n, b = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(n)]

def mul(mat1, mat2):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += mat1[i][k] * mat2[k][j] % 1000
    return res

def divAndCon(a, b):
    if b == 1:
        return a
    
    tmp = divAndCon(a, b//2)
    if b % 2 == 0:
        return mul(tmp, tmp)
    else:
        return mul(mul(tmp, tmp), a)

answer = divAndCon(mat, b)

for i in answer:
    for j in i:
        print(j % 1000, end=' ')
    print()