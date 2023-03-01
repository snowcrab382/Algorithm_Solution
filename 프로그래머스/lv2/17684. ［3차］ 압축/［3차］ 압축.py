def solution(msg):
    answer = []
    a = dict()
    for i in range(1,27):
        a[chr(i+64)] = i
    w,c = 0,0
    while True:
        c += 1
        if c == len(msg):
            answer.append(a[msg[w:c]])
            break
            
        if msg[w:c+1] not in a.keys():
            a[msg[w:c+1]] = len(a)+1
            answer.append(a[msg[w:c]])
            w = c   
    return answer