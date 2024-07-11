import sys
import heapq
MAX = sys.maxsize

def solution(stones, k):
    answer = MAX
    pq = []
    for i in range(k):
        heapq.heappush(pq, [-stones[i], i])
        
    i = k - 1
    while i < len(stones):
        heapq.heappush(pq, [-stones[i], i])
        
        while pq[0][1] < i - k + 1:
            heapq.heappop(pq)
        i += 1
        answer = min(answer, -pq[0][0])
    
    return answer

