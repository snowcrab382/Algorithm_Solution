from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
check = deque([int(input()) for _ in range(n)])
stack = [0]
queue = deque([i for i in range(1,n+1)])
result = []

while check:
    if stack[-1] == check[0]:
        stack.pop()
        check.popleft()
        result.append('-')
    else:
        if len(queue) == 0:
            print('NO')
            exit(0)
        else:
            stack.append(queue.popleft())
            result.append('+')
for i in result:
    print(i)