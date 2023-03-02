def solution(skill, skill_trees):
    a = []
    cnt = 0
    for x in range(1,len(skill)+1):
        a.append(skill[:x])
    
    for i in skill_trees:
        check = ''
        for j in i:
            if j in skill:
                check = check+j
        #i에 skill조합에 해당하는 경우가 아예 없는 경우도 배울 수 있기 때문에 cnt 해줘야함(check == '')
        if check == skill[:len(check)]:
            cnt += 1
    return cnt