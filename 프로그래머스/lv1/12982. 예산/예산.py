def solution(d, budget):
    cnt = 0
    d.sort()
    for i in d:
        budget -= i
        cnt += 1
        if budget == 0:
            return cnt
        elif budget < 0:
            return cnt-1
    return len(d)
        