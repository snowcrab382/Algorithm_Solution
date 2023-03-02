from collections import Counter

def solution(want, number, discount):
    answer = 0
    wanted = dict()
    for v,n in zip(want,number):
        wanted[v] = n
    
    for i in range(len(discount)-9):
        c = Counter(discount[i:i+10])
        if c == wanted:
            answer += 1
    return answer
    

