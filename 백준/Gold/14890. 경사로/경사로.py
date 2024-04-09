N, L = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

def check(line):
    slope = [False] * N
    for i in range(1, N):
        if abs(line[i-1] - line[i]) > 1:
            return False
        else:
            if line[i-1] - line[i] == 1:
                for j in range(L):
                    if i + j >= N:
                        return False
                    if line[i+j] != line[i]:
                        return False
                    if slope[i+j]:
                        return False
                    if not slope[i+j]:
                        slope[i+j] = True
            elif line[i-1] - line[i] == -1:
                for j in range(L):
                    if i - j - 1 < 0:
                        return False
                    if line[i-1-j] != line[i-1]:
                        return False
                    if slope[i-1-j]:
                        return False
                    if not slope[i-1-j]:
                        slope[i-1-j] = True
    return True

result = 0
for i in range(N):
    if check(graph[i]):
        result += 1
for j in range(N):
    if check([graph[i][j] for i in range(N)]):
        result += 1
print(result)