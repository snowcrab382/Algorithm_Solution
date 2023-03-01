def solution(elements):
    n = len(elements)
    elements *= 2
    result = set()
    
    for i in range(n):
        for j in range(n):
            result.add(sum(elements[j:j+i+1]))

    return len(result)