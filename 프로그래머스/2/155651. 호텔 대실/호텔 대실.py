def solution(book_time):
    timezone = [0] * (60 * 24 + 1)
    for start, end in book_time:
        idx_s = int(start[:2]) * 60 + int(start[3:])
        idx_e = int(end[:2]) * 60 + int(end[3:]) + 10
        if idx_e >= len(timezone):
            idx_e = len(timezone)
    
        for i in range(idx_s, idx_e):
            timezone[i] += 1
    
    answer = max(timezone)
    return answer