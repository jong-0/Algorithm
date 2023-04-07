import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
  cnt = 0
  case = int(input())
  li = [0] * case

  for i in range(case):
    ll = list(map(int, input().split()))
    li[i] = ll
  li.sort(key=lambda x:x[0])

  ck = [100001]
  for i in range(case):
    if ck[0] > li[i][1]:
      ck[0] = li[i][1]
    if 1 in li[i]:
      cnt += 1
    else:
      if ck[0] >= li[i][1]:
        cnt +=1

  print(cnt)