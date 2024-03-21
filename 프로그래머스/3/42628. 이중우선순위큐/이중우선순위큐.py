import heapq
def solution(operations):
    answer = [0,0]
    
    q = []
    for operation in operations:
        x, num = operation.split() 
        num = int(num)
        
        if x == 'I':
            heapq.heappush(q, num)
        elif x == 'D' and num == 1:
            if q:
                max_value = max(q)
                q.remove(max_value)
        else:
            if q:
                heapq.heappop(q)
    
    if q:
        answer = [max(q), heapq.heappop(q)]
        return answer
    else:
        return answer