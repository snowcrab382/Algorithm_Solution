def solution(s):
    answer = True
    stack = [0]
    for i in s:
        if i == ')' and stack[-1] == '(':
            stack.pop()
            continue
        stack.append(i)
    
    if len(stack) != 1:
        answer = False

    return answer