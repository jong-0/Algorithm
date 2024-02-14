from collections import deque

while True:
    n = input()
    if n == '.':
        break
    else:
        n = deque(n)
        stack = []
        for i in range(len(n)):
            if n[i] == '(' or n[i] == '[' or n[i] == ')' or n[i] == ']':
                stack.append(n[i])

            if len(stack) > 1 and stack[-1] == ')' and stack[-2] == '(':
                stack.pop()
                stack.pop()
            elif len(stack) > 1 and stack[-1] == ']' and stack[-2] == '[':
                stack.pop()
                stack.pop()

        if len(stack) > 0:
            print('no')
        else:
            print('yes')