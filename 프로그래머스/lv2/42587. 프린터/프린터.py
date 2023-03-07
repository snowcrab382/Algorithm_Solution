from collections import deque

def solution(priorities, location):
    a = [(i,j) for i,j in enumerate(priorities)]
    queue = deque(a)
    cnt = 0
    
    while True:
        x,y = queue.popleft()
        pri = True
        for i,j in queue:
            if y < j:
                pri = False
                queue.append((x,y))
                break
        if pri:
            cnt += 1
            if x == location:
                return cnt