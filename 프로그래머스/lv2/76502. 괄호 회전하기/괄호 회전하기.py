from collections import deque

def solution(s):
    queue = deque(s)
    cnt = 0
    start = 0
    while start < len(s):
        check = []
        
        for j in queue:
            if len(check) != 0 and check[-1] == '[' and j == ']':
                check.pop()
                continue
            if len(check) != 0 and check[-1] == '(' and j == ')':
                check.pop()
                continue
            if len(check) != 0 and check[-1] == '{' and j == '}':
                check.pop()
                continue
            check.append(j)
        
        if len(check) == 0:
            cnt += 1
        
        queue.append(queue.popleft())
        start += 1
        
    return cnt