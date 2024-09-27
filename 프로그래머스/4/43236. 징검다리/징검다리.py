def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    start, end = 1, distance
    while start <= end:
        mid = (start + end) // 2
        prev, cnt = 0, 0
        for rock in rocks:
            if rock - prev < mid:
                cnt += 1
                if cnt > n:
                    break
            else:
                prev = rock
        if cnt > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer