import heapq

def solution(n, k, enemy):
    answer = 0
    
    q = []
    for x in enemy:
        if n >= x:
            n -= x
            heapq.heappush(q, -x)
            
        else:
            if k:
                if q:
                    if x < -q[0]:
                        n += -heapq.heappop(q)
                        heapq.heappush(q, -x)
                        n -= x
                k -= 1
            else:
                break
        answer += 1
    
    return answer