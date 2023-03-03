import itertools

def solution(word):
    alpha = ['A','E','I','O','U'] * 5
    answer = set()
    for i in range(1,6):
        a = list(itertools.permutations(alpha,i))
        for j in range(len(a)):
            answer.add(''.join(a[j]))
    answer = sorted(list(answer))
    return answer.index(word)+1
        