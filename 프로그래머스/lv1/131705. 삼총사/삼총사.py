cnt = 0
result = []
visited = [0]*14

def check(number, student,start):
    global cnt
    if student == 3 and sum(result) == 0:
        print(result)
        cnt += 1
        return

    for i in range(start,len(number)):
        if not visited[i]:
            result.append(number[i])
            visited[i] = 1
            check(number, student + 1,i+1)
            result.pop()
            visited[i] = 0

def solution(number):
    check(number,0,0)
    
    return cnt
    