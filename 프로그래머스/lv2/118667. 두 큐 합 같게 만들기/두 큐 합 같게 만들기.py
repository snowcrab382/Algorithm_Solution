from collections import deque

def solution(queue1, queue2):
    queue1,queue2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    
    for i in range(300000):
        if q1_sum == q2_sum:
            return i
        elif q2_sum > q1_sum:
            tmp = queue2.popleft()
            queue1.append(tmp)
            q1_sum += tmp
            q2_sum -= tmp
        elif q1_sum > q2_sum:
            tmp = queue1.popleft()
            queue2.append(tmp)
            q2_sum += tmp
            q1_sum -= tmp
            
    return -1
    