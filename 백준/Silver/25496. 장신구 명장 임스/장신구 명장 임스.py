import sys
input = sys.stdin.readline

p, n = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

cnt = 0
for i in range(n):
  if p < 200:
    p += li[i]
    cnt += 1
  else:
    break

print(cnt)