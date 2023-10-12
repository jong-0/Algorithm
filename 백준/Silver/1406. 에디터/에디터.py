import sys

l = list(sys.stdin.readline().rstrip())
r = []

n = int(sys.stdin.readline())
for _ in  range(n):
    a = sys.stdin.readline().split()

    if a[0] == 'L':
        if l:
            r.append(l.pop())
    elif a[0] == 'D':
        if r:
            l.append(r.pop())
    elif a[0] == 'B':
        if l:
            l.pop()
    else:
        l.append(a[1])

l.extend(reversed(r))
print(''.join(l))