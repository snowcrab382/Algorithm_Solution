def solution(numbers):
    numbers.sort()
    result = set()
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            result.add(numbers[i]+numbers[j])
    return sorted(list(result))