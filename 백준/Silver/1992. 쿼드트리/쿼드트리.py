N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int,input())))

def solve(x,y,n):
    check = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != graph[i][j]:
                check = -1
                break

    if check == -1:
        print('(', end='')
        n //= 2
        solve(x,y,n)
        solve(x,y+n,n)
        solve(x+n,y,n)
        solve(x+n,y+n,n)
        print(')', end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')

solve(0,0,N)