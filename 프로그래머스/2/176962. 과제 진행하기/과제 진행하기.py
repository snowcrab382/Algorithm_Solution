def solution(plans):
    for i in plans:
        i[1] = int(i[1][:2]) * 60 + int(i[1][3:])
        i[2] = int(i[2])
    plans.sort(key = lambda x : x[1])
    
    wait = []
    time = 0
    answer = []
    for i in range(len(plans)-1):
        if plans[i+1][1] < plans[i][1] + plans[i][2]:
            remain = plans[i][1] + plans[i][2] - plans[i+1][1]
            wait.append((plans[i][0], remain))
        elif plans[i+1][1] > plans[i][1] + plans[i][2]:
            answer.append(plans[i][0])
            time = plans[i+1][1] - plans[i][1] - plans[i][2]
            
            while wait:
                n, r = wait.pop()
                
                if time >= r:
                    answer.append(n)
                    time -= r
                else:
                    wait.append((n, r - time))
                    break
        else:
            answer.append(plans[i][0])
    answer.append(plans[len(plans)-1][0])
    while wait:
        n, r = wait.pop()
        answer.append(n)
                
    return answer