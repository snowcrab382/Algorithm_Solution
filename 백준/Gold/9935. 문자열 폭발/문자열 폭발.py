sentence = input()
bomb = input()

stack = []
bomb_len = len(bomb)

for i in range(len(sentence)):
    stack.append(sentence[i])
    if ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

# 결과 출력
if stack:
    print(''.join(stack))
else:
    print('FRULA')