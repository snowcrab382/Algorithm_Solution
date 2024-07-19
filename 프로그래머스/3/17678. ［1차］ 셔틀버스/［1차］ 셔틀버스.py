import heapq

def solution(n, t, m, timetable):
    def transform(time):
        return int(time[:2]) * 60 + int(time[3:])
    
    start = transform("09:00") - t
    heap = []
    for i in timetable:
        heapq.heappush(heap, transform(i))
    
    for i in range(n):
        start += t
        answer = start
        cnt = m
        while heap:
            if heap[0] <= start and cnt:
                tmp = heapq.heappop(heap)
                cnt -= 1
            else:
                break
        if not cnt:
            answer = tmp - 1
            
    result = ''
    hour, minute = answer // 60, answer % 60
    if hour < 10:
        result += '0'
    result += str(hour) + ':'
    
    if minute < 10:
        result += '0'
    result += str(minute)
    
    return result