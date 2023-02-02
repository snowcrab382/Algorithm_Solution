l,c = map(int,input().split())
graph = sorted(list(input().split()))
ans = []
collection = ['a','e','i','o','u']

def solve(x,start):
    if x == l:
        cnt_c = 0
        for i in ans:
            if i in collection:
                cnt_c += 1
        if 1 <= cnt_c <= l-2:
            for i in ans:
                print(i, end='')
            print()
            return

    for i in range(start,c):
        ans.append(graph[i])
        solve(x+1,i+1)
        ans.pop()

solve(0,0)