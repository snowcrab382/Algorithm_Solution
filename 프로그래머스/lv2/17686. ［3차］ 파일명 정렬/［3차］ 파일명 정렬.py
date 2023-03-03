def solution(files):
    answer = []
    for i in files:
        f = []
        for j in range(len(i)):
            if i[j].isdigit():
                f.append(i[:j])
                for k in range(j,len(i)):
                    if k == len(i)-1 and i[k].isdigit():
                        f.append(i[j:])
                        break
                    if not i[k].isdigit():
                        f.append(i[j:k])
                        f.append(i[k:])
                        break
                    
                break
        answer.append(f)
        
    answer.sort(key = lambda x : (x[0].lower(),int(x[1])))
    for x in range(len(answer)):
        answer[x] = ''.join(answer[x])
    return answer