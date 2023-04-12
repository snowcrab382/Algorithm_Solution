from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []
    for i in course:
        tmp = []
        for j in orders:
            combi = combinations(sorted(j),i)
            tmp += combi
        counter = Counter(tmp)

        if len(counter) != 0 and max(counter.values()) != 1:
            result += [''.join(k) for k in counter if counter[k] == max(counter.values())]
    
    return sorted(result)