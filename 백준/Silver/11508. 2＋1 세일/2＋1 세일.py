n = int(input())
li = [0]*n
for i in range(n):
    li[i] = int(input())

li.sort(reverse=True)
sum = 0
cnt = 0

for i in li:
    cnt += 1
    if cnt%3==0:
        continue
    else:
        sum+=i

print(sum)