n = int(input())
cnt = 0
for i in range(1,n+1):
  ans = i + sum(list(map(int, list(str(i)))))
  if ans == n:
    cnt += 1
    print(i)
    break

if cnt == 0:
  print(0)