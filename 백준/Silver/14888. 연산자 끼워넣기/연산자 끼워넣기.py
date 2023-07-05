import sys

n = int(input())
a = list(map(int,input().split()))
op = list(map(int,input().split()))
maxi,mini = -sys.maxsize,sys.maxsize

def bt(sum,idx,add,sub,mul,div):
    global maxi,mini
    if idx == n:
        maxi = max(maxi,sum)
        mini = min(mini,sum)
        return

    if add > 0:
        bt(sum + a[idx], idx + 1, add - 1, sub, mul, div)
    if sub > 0:
        bt(sum - a[idx], idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        bt(sum * a[idx], idx + 1, add, sub, mul - 1, div)
    if div > 0:
        bt(int(sum / a[idx]), idx + 1, add, sub, mul, div - 1)

bt(a[0],1,op[0],op[1],op[2],op[3])
print(maxi)
print(mini)