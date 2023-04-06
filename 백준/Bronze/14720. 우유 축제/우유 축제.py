n = int(input())
li = list(map(int, input().split()))
cnt = 0

for i in range(n):
  if cnt%3 == 0 and li[i] == 0:
    cnt += 1
  elif cnt%3 == 1 and li[i] == 1:
    cnt += 1
  elif cnt%3 == 2 and li[i] == 2:
    cnt += 1

print(cnt)