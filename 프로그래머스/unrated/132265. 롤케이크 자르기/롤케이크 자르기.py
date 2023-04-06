from collections import Counter

def solution(topping):
    cnt = Counter(topping)
    cnt_set = set()
    answer = 0
    for i in topping:
        cnt[i] -= 1
        cnt_set.add(i)
        if cnt[i] == 0:
            cnt.pop(i)
        if len(cnt) == len(cnt_set):
            answer += 1
    return answer