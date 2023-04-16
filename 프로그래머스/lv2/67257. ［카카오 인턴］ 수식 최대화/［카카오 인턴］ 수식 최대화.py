from itertools import permutations

def solution(expression):
    tmp = ""
    op = ['-','+','*']
    answer = 0
    for i in permutations(op,3):
        a = i[0]
        b = i[1]
        tmp_list = []
        for j in expression.split(a):
            tmp = [f"({k})" for k in j.split(b)]
            tmp_list.append(f"({b.join(tmp)})")
        answer = max(answer,abs(eval(a.join(tmp_list))))
    return answer