import sys
input = sys.stdin.readline

n = map(int, input().split())
li = list(map(int, input().rstrip().split()))

chk = [0] * (len(li) - 1)
chk[0] = li[0]
for i in range(1, len(li)-1):
    chk[i] = chk[i-1] + li[i]

sum = 0
for i in range(len(chk)):
    sum += chk[i] * li[i+1]

print(sum)