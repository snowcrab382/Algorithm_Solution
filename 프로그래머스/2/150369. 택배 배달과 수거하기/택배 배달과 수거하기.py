from collections import deque

def solution(cap, n, deliveries, pickups):
    answer = 0
    d_q = deque([d for d in sorted(enumerate(deliveries), reverse = True) if d[1]])
    p_q = deque([p for p in sorted(enumerate(pickups), reverse = True) if p[1]])
    
    while d_q or p_q:
        distance_d, distance_p = 0, 0
        if d_q:
            distance_d = d_q[0][0] + 1
            tmp_d_c = cap
            while d_q:
                if not tmp_d_c:
                    break
                    
                d_i, d_c = d_q.popleft()
                if d_c >= tmp_d_c:
                    d_c -= tmp_d_c
                    tmp_d_c = 0
                    if d_c:
                        d_q.appendleft((d_i, d_c))
                        break
                else:
                    tmp_d_c -= d_c
        
        if p_q:
            distance_p = p_q[0][0] + 1
            tmp_p_c = cap
            while p_q:
                if not tmp_p_c:
                    break
                    
                p_i, p_c = p_q.popleft()
                if p_c >= tmp_p_c:
                    p_c -= tmp_p_c
                    tmp_p_c = 0
                    if p_c:
                        p_q.appendleft((p_i, p_c))
                        break
                else:
                    tmp_p_c -= p_c
                
        answer += 2 * max(distance_d, distance_p)
    return answer

# [1, 0, 1, 0, 0, 0, 0]
# [0, 1, 0, 0, 0, 0, 0]
# 14
# 10
# 6