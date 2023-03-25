def solution(n, k):
    dp = [0] * 21
    dp[1] = 1
    dp[2] = 2
    for i in range(3,21):
        dp[i] = dp[i-1]*i
    
    result = []
    numbers = [i for i in range(1,n+1)]
    while n != 0:
        num = dp[n]//n
        idx = k // num
        k %= num
        
        if k == 0:
            result.append(numbers.pop(idx-1))
        else:
            result.append(numbers.pop(idx))
        n -= 1
    return result