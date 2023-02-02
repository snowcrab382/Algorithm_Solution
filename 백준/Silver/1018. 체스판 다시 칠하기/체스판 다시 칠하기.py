N,M = map(int,input().split())
chess = []
count = set()

for _ in range(N):
    chess.append(input())

for x in range(N-7):
    for y in range(M-7):
        first_W = 0
        first_B = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i+j) % 2 == 0:
                    if chess[i][j] != 'W':
                        first_W += 1
                    if chess[i][j] != 'B':
                        first_B += 1
                else:
                    if chess[i][j] != 'B':
                        first_W += 1
                    if chess[i][j] != 'W':
                        first_B += 1
        count.add(min(first_W,first_B))

print(min(count))