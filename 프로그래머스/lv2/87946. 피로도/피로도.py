def bt(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = 1
            bt(k-dungeons[i][1],cnt+1,dungeons)
            visited[i] = 0

def solution(k, dungeons):
    global visited
    visited = [0] * len(dungeons)
    bt(k, 0,dungeons)
    return answer

cnt = 0
answer = 0
visited = []