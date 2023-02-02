import sys
from collections import deque

input = sys.stdin.readline
queue = deque([])

N = int(input())
for _ in range(N):
    order = input().split()
    target = order[0]

    if target == 'push_front':
        queue.appendleft(int(order[1]))
    elif target == 'push_back':
        queue.append(int(order[1]))
    elif target == 'pop_front':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print('-1')
    elif target == 'pop_back':
        if len(queue) != 0:
            print(queue.pop())
        else:
            print('-1')
    elif target == 'size':
        print(len(queue))
    elif target == 'empty':
        if len(queue) != 0:
            print(0)
        else:
            print(1)
    elif target == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print('-1')
    elif target == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print('-1')