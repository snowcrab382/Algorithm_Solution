import sys; input = sys.stdin.readline
import copy

# CCTV 종류별, 바라보는 방향별 감시영역 재귀적 탐색
def dfs(graph, depth):
    global answer
    # 종료 조건: 모든 CCTV 탐색
    if depth == len(cctv_list):
        # 사각지대 최솟값
        answer = min(answer, count_zero(graph))
        return
    else:
        # 사무실 정보 깊은 복사
        graph_copy = copy.deepcopy(graph)
        x, y, cctv_type = cctv_list[depth]
        for cctv_dir in cctv_direction[cctv_type]:
            # CCTV 감시영역 구하는 함수 호출
            watch(x, y, cctv_dir, graph_copy)
            # 현재 Case에서 타 모든 CCTV 재귀적 탐색
            dfs(graph_copy, depth + 1)
            # CCTV를 다른 방향으로 회전시킨 후 재탐색하기 위함
            graph_copy = copy.deepcopy(graph)

# CCTV 감시영역 구하는 함수
def watch(x, y, direction, graph):
    for d in direction:
        nx, ny = x, y
        # 특정 방향으로 벽을 만나거나 사무실을 벗어나기 전까지 탐색
        while True:
            nx += direction_list[d][0]
            ny += direction_list[d][1]
            # 맵 내 위치
            if 0 <= nx < N and 0 <= ny < M:
                # 벽을 만난 경우
                if graph[nx][ny] == 6:
                    break
                elif graph[nx][ny] == 0:
                    graph[nx][ny] = '#'
            else:
                break

def count_zero(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = int(1e9)
    cctv_list = []
    for i in range(N):
        for j in range(M):
            if 1 <= graph[i][j] <= 5:
                cctv_list.append((i, j, graph[i][j]))
    direction_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cctv_direction = [
        [],
        [[0], [1], [2], [3]], # 1번 CCTV
        [[0, 1], [2, 3]], # 2번 CCTV
        [[0, 2], [0, 3], [1, 2], [1, 3]], # 3번 CCTV
        [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], # 4번 CCTV
        [[0, 1, 2, 3]] # 5번 CCTV
    ]
    dfs(graph, 0)
    print(answer)