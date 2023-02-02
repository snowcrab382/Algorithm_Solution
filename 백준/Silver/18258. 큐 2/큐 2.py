import sys
from collections import deque
input = sys.stdin.readline

queue = deque([])
N = int(input())
for _ in range(N):
    order = input().strip().split()
    if len(order) != 2:
        target = order[0]
        if target == 'pop':
            if len(queue) == 0:
                print('-1')
            else:
                print(queue.popleft())
        elif target == 'size':
            print(len(queue))
        elif target == 'empty':
            if len(queue) != 0:
                print('0')
            else:
                print('1')
        elif target == 'front':
            if len(queue) == 0:
                print('-1')
            else:
                print(queue[0])
        else:
            if len(queue) == 0:
                print('-1')
            else:
                print(queue[-1])
    else:
        queue.append(int(order[1]))