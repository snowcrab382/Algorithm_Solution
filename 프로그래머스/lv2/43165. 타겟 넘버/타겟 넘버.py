def solution(numbers, target):
    minus = (sum(numbers)-target)//2
    
    def dfs(x,start):
        global cnt
        if x == minus:
            cnt += 1
        
        for i in range(start,len(numbers)):
            x += numbers[i]
            dfs(x,i+1)
            x -= numbers[i]
    
    dfs(0,0)
    return cnt
cnt = 0