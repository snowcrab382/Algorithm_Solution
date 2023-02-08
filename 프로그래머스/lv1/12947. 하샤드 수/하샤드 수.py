def solution(x):
    result = []
    for i in str(x):
        result.append(int(i))
    if x % sum(result) == 0:
        return True
    return False