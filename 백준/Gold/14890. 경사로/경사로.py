n, l = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
result = 0

def check(line):
    slope = [False] * n
    for i in range(1, n):
        if abs(line[i-1] - line[i]) > 1:
            return False
        else:
            if line[i-1] - line[i] == 1: #오르막
                for j in range(l):
                    if i + j >= n:
                        return False
                    if line[i] != line[i+j]:
                        return False
                    if slope[i+j]:
                        return False
                    if not slope[i+j]:
                        slope[i+j] = True
            elif line[i-1] - line[i] == -1: #내리막
                for j in range(l):
                    if i - j - 1< 0:
                        return False
                    if line[i-1] != line[i-j-1]:
                        return False
                    if slope[i-j-1]:
                        return False
                    if not slope[i-j-1]:
                        slope[i-j-1] = True
    return True

for i in range(n):
    if check(graph[i]):
        result += 1
for j in range(n):
    if check([graph[i][j] for i in range(n)]):
        result += 1
print(result)