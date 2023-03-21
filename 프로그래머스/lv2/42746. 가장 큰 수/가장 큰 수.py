def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key = lambda x : x*3,reverse = True)
    
    result = ''.join(numbers)
    if result[0] == '0':
        return '0'
    else:
        return result
# def solution(numbers):    
#     s = list(map(str,numbers))
#     a = sorted(s,key=lambda x: x*3,reverse=1)
#     return str(int("".join(a)))