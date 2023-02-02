def solve(x,start):
    if x == 6:
        for i in ans:
            print(i, end=' ')
        print()
        return

    for i in range(start,k):
        ans.append(graph[i])
        solve(x+1,i+1)
        ans.pop()

while True:
    graph = list(map(int, input().split()))
    if graph[0] == 0:
        break
    k = graph.pop(0)
    ans = []

    solve(0,0)
    print()