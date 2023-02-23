def solution(n):
    one = bin(n).count('1')
    i = n+1
    while bin(i).count('1') != one:
        i += 1
    
    return i