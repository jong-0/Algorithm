n = int(input())
li = list(map(int, input().split()))

li.sort()

ll = [0] * n

for i in range(n):
  ll[i] = li[i+n]

print(ll[-1] - ll[0])