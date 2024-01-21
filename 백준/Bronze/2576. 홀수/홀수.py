li = []
sum = 0

for _ in range(7):
    n = int(input())
    if n%2==1:
        sum += n
        li.append(n)
    else:
        continue

if len(li) == 0:
    print(-1)
else:
    li.sort()
    print(sum)
    print(li[0])