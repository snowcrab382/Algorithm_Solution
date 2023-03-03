import itertools

def solution(word):
    alpha = ['A','E','I','O','U'] * 5
    answer = []
    for i in range(1,6):
        for j in set(itertools.permutations(alpha,i)):
            answer.append(''.join(j))
            
    return sorted(answer).index(word)+1
        