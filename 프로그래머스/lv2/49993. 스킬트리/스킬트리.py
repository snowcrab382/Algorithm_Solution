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
        if check in a or check == '':
            cnt += 1
    return cnt