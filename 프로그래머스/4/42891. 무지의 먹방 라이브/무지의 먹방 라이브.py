from heapq import heappush, heappop

def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
    
    food_heap = []
    length = len(food_times)
    for idx, food in enumerate(food_times):
        heappush(food_heap, [food, idx + 1])
    
    time = 0
    while (food_heap[0][0] - time) * length < k:
        k -= (food_heap[0][0] - time) * length
        time += (food_heap[0][0] - time)
        length -= 1
        heappop(food_heap)
        
    result = sorted(food_heap, key = lambda x : x[1])
    answer = result[k % length][1]
    return answer
