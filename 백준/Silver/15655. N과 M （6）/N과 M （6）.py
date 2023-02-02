n,m = map(int,input().split())
arr = [0] * 10
isused = [0] * 10
num = sorted(list(map(int,input().split())))

def func(k):
    if k == m:
        for i in range(m):
            print(num[arr[i]], end=' ')
        print()
        return

    st = 0
    if k != 0:
        st = arr[k-1] + 1
    for i in range(st,n):
        if not isused[i]:
            arr[k] = i
            isused[i] = 1
            func(k+1)
            isused[i] = 0

func(0)