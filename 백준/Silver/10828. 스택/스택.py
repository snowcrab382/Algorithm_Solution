import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    order = input().split()
    target = order[0]
    if target == 'push':
        stack.append(order[1])
    elif target == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print('-1')
    elif target == 'size':
        print(len(stack))
    elif target == 'empty':
        if len(stack) != 0:
            print('0')
        else:
            print('1')
    elif target == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print('-1')