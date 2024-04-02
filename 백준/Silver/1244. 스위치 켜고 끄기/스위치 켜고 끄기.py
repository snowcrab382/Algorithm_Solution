n = int(input())
switch = [0] + list(map(int,input().split()))
k = int(input())

def change(i):
    if switch[i]:
        switch[i] = 0
    else:
        switch[i] = 1

for _ in range(k):
    g, num = map(int,input().split())
    if g == 1:
        for i in range(num, n+1, num):
            change(i)
    else:
        change(num)
        for i in range(n//2):
            if num - i < 1 or num + i > n:
                break
            if switch[num-i] == switch[num+i]:
                change(num-i)
                change(num+i)
            else:
                break
for i in range(1, n+1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()