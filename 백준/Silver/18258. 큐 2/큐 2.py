import sys
input = sys.stdin.readline

from collections import deque
q = deque()

num = int(input())

for _ in range(num):
  s = input().split()

  if s[0] == 'push':
    q.append(s[1])
  elif s[0] == 'pop':
    if len(q) < 1:
      print(-1)
    else:
      print(q[0])
      q.popleft()
  elif s[0] == 'size':
    print(len(q))
  elif s[0] == 'empty':
    if len(q) < 1:
      print(1)
    else:
      print(0)
  elif s[0] == 'front':
    if len(q) < 1:
      print(-1)
    else:
      print(q[0])
  else:
    if len(q) < 1:
      print(-1)
    else:
      print(q[-1])