def solution(n):
    result = []
    for i in reversed(str(n)):
        result.append(int(i))
    return result