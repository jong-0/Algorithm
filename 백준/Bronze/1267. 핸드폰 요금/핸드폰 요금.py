import sys
input = sys.stdin.readline

num = int(input())
li = list(map(int, input().split()))

Y = 0
M = 0

for i in li:
    Y += (i//30 + 1) * 10
    M += (i//60 + 1) * 15

if Y == M:
    print('Y M', Y)
elif Y > M:
    print('M', M)
else:
    print('Y', Y)