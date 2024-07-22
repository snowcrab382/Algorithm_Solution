def solution(enroll, referral, seller, amount):
    
    def distribute(idx, pay):
        d = pay // 10
        result[idx] += pay - d
        if graph[idx] == -1 or pay < 10:
            return
        distribute(graph[idx], d)


    enrolls = dict()
    for idx, e in enumerate(enroll):
        enrolls.setdefault(e, idx)

    graph = [0] * len(enroll)
    for idx, r in enumerate(referral):
        if r == '-':
            graph[idx] = -1
        else:
            graph[idx] = enrolls[r]

    result = [0] * len(enroll)
    for i in range(len(seller)):
        s, a = seller[i], amount[i] * 100
        distribute(enrolls[s], a)
    
    return result

    