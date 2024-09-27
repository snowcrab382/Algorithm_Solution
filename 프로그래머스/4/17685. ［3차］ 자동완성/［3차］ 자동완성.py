def solution(words):
    words.sort()
    n = len(words)
    result = [0] * n
    for i in range(n - 1):
        a = len(words[i])
        b = len(words[i + 1])
        for j in range(min(a, b)):
            if words[i][j] != words[i + 1][j]:
                j -= 1
                break
        result[i] = max(result[i], min(a, j + 2))
        result[i + 1] = max(result[i + 1], min(b, j + 2))
    
    return sum(result)