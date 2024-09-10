from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''

    # 좌표 토대로 남은 거리 계산
    def manhattan(x1, y1):
        return abs(x1 - (r-1)) + abs(y1-(c-1))

    # k가 최단 거리보다 작거나, 최단 거리 - k가 홀수라면 도착지에 k번만에 도착 불가
    if manhattan(x-1, y-1) > k or (manhattan(x-1, y-1) - k) % 2:
        return 'impossible'
    
    # 탐색 방향 사전순으로 - d l r u
    dir = [[1, 0, 'd'], [0, -1, 'l'], [0, 1, 'r'], [-1, 0, 'u']]
    q = deque()
    q.append((x-1, y-1, 0, ''))
    while q:
        a, b, cnt, path = q.popleft()
        # 도착했는데 남은 거리가 홀수라면 조건 달성 불가
        if (a, b) == (r-1, c-1) and (k-cnt) % 2:
            return 'impossible'
        # 조건 달성. 결과 반환
        elif (a, b) == (r-1, c-1) and cnt == k:
            return path
        for da, db, next_path in dir:
            na = a + da
            nb = b + db
            if 0<=na<n and 0<=nb<m:
                # 다음 이동 자리를 보는 것이므로 +1 을 해주어야 함
                if manhattan(na, nb) + cnt + 1 > k:
                    continue
                q.append((na, nb, cnt+1, path + next_path))
                break

    return answer
