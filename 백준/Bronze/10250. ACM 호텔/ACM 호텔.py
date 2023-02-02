T = int(input())
for i in range(T):
    H,W,N = map(int,input().split())
    if N % H == 0:
        height = str(H)
        wide = str(N // H)
        if int(wide) < 10:
            wide = str('0')+wide
        print(height+wide)
    else:
        height = str(N % H)
        wide = str( N // H + 1)
        if int(wide) < 10:
            wide = str('0')+wide
        print(height+wide)