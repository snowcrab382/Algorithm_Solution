from collections import deque

def solution(number, k):
    result = []
    for i in number:
        while k > 0 and len(result) != 0 and result[-1] < i:
            result.pop()
            k -= 1
        result.append(i)

    return ''.join(result[:len(number)-k]) #number="11",k=1 일 때, result =['1','1']이 됨
    