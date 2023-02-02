N,S = map(int,input().split())
cnt = 0
ans = []
arr = list(map(int,input().split()))

def solve(start):
    global cnt
    if sum(ans) == S and len(ans)>0:
        cnt += 1
    
    for i in range(start,N):
        ans.append(arr[i])
        solve(i+1)
        ans.pop()
        
solve(0)
print(cnt)