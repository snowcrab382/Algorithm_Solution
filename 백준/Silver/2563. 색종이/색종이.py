paper = [[0 for i in range(100)]for j in range(100)]
count = 0
N = int(input())

for _ in range(N):
    x,y = map(int,input().split())
    for i in range(y,y+10):
        if i > 99:
            break
        for j in range(x,x+10):
            if j > 99:
                break
            paper[i][j] = 1

for a in range(len(paper)):
    count += paper[a].count(1)
print(count)