from itertools import product

def solution(users, emoticons):
    answer = []
    users.sort()
    for p in product([10,20,30,40], repeat = len(emoticons)):
        plus, total = 0, 0
        for user in users:
            buy = 0
            for idx, discount in enumerate(p):
                if discount >= user[0]:
                    buy += emoticons[idx] * ((100 - discount) / 100)
                    
            if buy >= user[1]:
                plus += 1
            else:
                total += buy

        answer.append((plus, total))
    answer.sort(key = lambda x : (-x[0], -x[1]))

    return answer[0]