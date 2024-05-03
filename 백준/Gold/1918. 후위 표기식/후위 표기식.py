notation = input()
stack = []
ans = ''

for i in notation:
    if i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            ans += stack.pop()
        stack.append(i)
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(i)
    else:
        ans += i
while stack:
    ans += stack.pop()
print(ans)