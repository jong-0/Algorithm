import sys
input = sys.stdin.readline

num = int(input())
li = list(map(int, input().rstrip().split()))

for i in range(1,num):
  li[i] = li[i-1] + li[i]
li = [0] + li

n = int(input())
for _ in range(n):
  a, b = map(int, input().split())
  print(li[b] - li[a-1])