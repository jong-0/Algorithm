n, l, k = map(int, input().split())
score = 0
num = 0
li = [0] * n

for i in range(n):
  ll = list(map(int, input().split()))
  li[i] = ll

li.sort(key=lambda x:x[1])

for i in range(n):
  if li[i][1] <= l:
    score+=140
    num+=1
  else:
    if li[i][0] <= l:
      score+=100
      num+=1

  if num == k:
    break

print(score)