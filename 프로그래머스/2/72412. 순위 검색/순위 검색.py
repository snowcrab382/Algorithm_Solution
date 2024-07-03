def solution(info, query):
    answer = []
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data[(a, b, c, d)] = []
    
    infos = [i.split() for i in info]
    infos.sort(key = lambda x : int(x[4]))
    
    for a,b,c,d,score in infos:
        for x in [a, '-']:
            for y in [b, '-']:
                for z in [c, '-']:
                    for k in [d, '-']:
                        data[(x,y,z,k)].append(int(score))
    
    for q in query:
        a, b, c, d, score = q.replace("and","").split()
        length = len(data[(a,b,c,d)])
        start, end = 0, length
        while start < end:
            mid = (start + end) // 2
            if data[(a,b,c,d)][mid] >= int(score):
                end = mid
            else:
                start = mid + 1
        answer.append(length - start)
        
    return answer