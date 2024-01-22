li = [0] * 9

for i in range(9):
    li[i] = int(input())

cnt = sum(li)
cnt = cnt - 100

i, j = 0, 1
while True:
    if li[i] + li[j] == cnt:
        li.remove(li[j])
        li.remove(li[i])
        break
    else:
        if j == len(li) - 1:
            i += 1
            j = i + 1
        else:
            j += 1

li.sort()
for i in li:
    print(i)