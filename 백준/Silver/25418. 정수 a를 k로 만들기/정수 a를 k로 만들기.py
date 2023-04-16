import sys
input = sys.stdin.readline

a, k = map(int, input().split())
count = 0
while True:
  if k%2 == 1:
    k -= 1
    count += 1
  else:
    k = k/2
    count += 1
  
  if k == a:
    print(count)
    break
  if k < a:
    k = k*2
    count-=1
    print(int(count-a+k))
    break