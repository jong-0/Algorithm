from collections import deque

n = int(input())
for _ in range(n):
    s = deque(input())
    stack = []

    for i in range(len(s)):
        stack.append(s.popleft())

        if len(stack) > 1 and stack[-1] == ')' and stack[-2] == '(':
            stack.pop()
            stack.pop()

    if len(stack) > 0:
        print('NO')
    else:
        print('YES')