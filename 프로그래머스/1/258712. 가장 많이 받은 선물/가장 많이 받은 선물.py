def solution(friends, gifts):
    
    dic = {}
    for idx, friend in enumerate(friends):
        dic[friend] = idx
    print(dic)
    
    leng = len(friends)
    graph = [[0] * leng for _ in range(leng)]
    
    score = [0] * leng
    answer = [0] * leng
    
    for gift in gifts:
        a, b = gift.split()
        x, y = dic[a], dic[b]
        score[x] += 1
        score[y] -= 1
        
        graph[x][y] += 1
    
    for i in graph:
        print(i)
    print(score)
    for i in range(leng):
        for j in range(i, leng):
            if i == j:
                continue
            a, b = graph[i][j], graph[j][i]
            
            if a > b:
                answer[i] += 1
            elif b > a:
                answer[j] += 1
            else:
                print(i,j, score[i], score[j])
                if score[i] == score[j]:
                    continue
                    
                if score[i] > score[j]:
                    answer[i] += 1
                else:
                    answer[j] += 1
    return max(answer)
                
            
    
    return answer
