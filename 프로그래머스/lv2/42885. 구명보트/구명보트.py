from collections import deque

def solution(people, limit):
    queue = deque(sorted(people))
    cnt = 0
    while len(queue)>1:
        if queue[0] + queue[-1] > limit:
            queue.pop()
        else:
            queue.popleft()
            queue.pop()
        cnt += 1
    if len(queue) != 0:
        cnt += len(queue)
    return cnt
    