from collections import deque
import sys

# 동,남,서,북
dx = [0,1,0,-1]
dy = [1,0,-1,0]


def solution(rows, columns, queries):
    graph = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    answer = []

    for query in queries:
        sX, sY, eX, eY = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        MIN = sys.maxsize

        x, y, tmp, idx = sX, sY, graph[sX][sY], 0
        while True:
            nx = x + dx[idx]
            ny = y + dy[idx]

            if not sX <= nx <= eX or not sY <= ny <= eY:
                if idx == 3:
                    answer.append(MIN)
                    break
                idx += 1
                continue

            next = graph[nx][ny]
            graph[nx][ny] = tmp
            tmp = next

            x, y = nx, ny
            MIN = min(MIN, tmp)
    return answer
