import heapq

def solution(scoville, K):
    cnt = 0
    scoville.sort()
    while scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville,a+b*2)
        cnt += 1
        if len(scoville) == 1:
            break
    if scoville[0] <K:
        return -1
    else:
        return cnt
        