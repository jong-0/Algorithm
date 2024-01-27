n = int(input())

li = list(map(int, input().split()))
chk = [0] * (n-1)
chk[0] = li[0]

for i in range(1, len(chk)):
    chk[i] = chk[i-1] + li[i]

sum = 0
for i in range(len(chk)):
    sum += chk[i] * li[i+1]

print(sum%1000000007)