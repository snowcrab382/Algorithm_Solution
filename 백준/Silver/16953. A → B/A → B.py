a,b = map(int,input().split())
answer = -1

def bt(a,b,c):
    global answer
    if a == b:
        answer = c
        return
    if a < b:
        for i in [a*2,int(str(a)+'1')]:
            bt(i,b,c+1)
    else:
        return False

bt(a,b,1)
print(answer)