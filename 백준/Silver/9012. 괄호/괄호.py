from collections import deque

a = int(input())
for _ in range(a):
  flag = True
  case = deque(input())
  stack = []
  while case:
    temp = case.popleft()
    if temp == '(':
      stack.append(temp)
    else:
      if len(stack) != 0:
        stack.pop()
      else:
        flag = False
        continue
  if len(stack) != 0 or not flag:
    print('NO')
  else:
    print('YES')