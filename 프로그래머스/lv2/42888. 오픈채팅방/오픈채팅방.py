def solution(record):
    a = dict()
    check = []
    answer = []
    for i in record:
        check.append(i.split())
    
    for j in check:
        if j[0] == 'Enter':
            a[j[1]] = j[2]
        elif j[0] == 'Change':
            a[j[1]] = j[2]
    
    for k in check:
        if k[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(a[k[1]]))
        elif k[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(a[k[1]]))
    return answer