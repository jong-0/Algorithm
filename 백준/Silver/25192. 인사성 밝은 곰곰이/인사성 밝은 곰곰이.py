import sys
input = sys.stdin.readline

n = int(input())

li = set([])
ans = 0

for i in range(n):
  s = input()
  if s == 'ENTER\n':
    ans += len(li)
    li = set([])
  else:
    li.add(s)

ans += len(li)
print(ans)