from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, j, cost, board, r, c):
    visited = [[0] * c for _ in range(r)]
    queue = deque()
    queue.append((i, j, cost))

    while queue:
        x, y, cnt = queue.popleft()

        if board[x][y] == 'G':
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while True:
                if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != 'D':
                    nx += dx[i]
                    ny += dy[i]
                else:
                    nx -= dx[i]
                    ny -= dy[i]
                    break
            if not visited[nx][ny]:
                visited[nx][ny] = cnt + 1
                queue.append((nx, ny, cnt + 1))
    return -1

def solution(board):
    r, c = len(board), len(board[0])
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                return bfs(i, j, 0, board, r, c)
