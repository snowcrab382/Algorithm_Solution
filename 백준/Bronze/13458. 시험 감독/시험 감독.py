import sys
input = sys.stdin.readline
N = int(input())
A = map(int,input().split())
B, C = map(int,input().split())
count = 0
for i in A:
    if i <= B:
        count += 1
    else:
        i -= B
        count += 1
        if i % C == 0:
            count += i // C
        else:
            count += (i // C) + 1
print(count)