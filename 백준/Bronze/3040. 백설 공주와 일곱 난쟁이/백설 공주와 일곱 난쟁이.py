li = []
for _ in range(9):
    li.append(int(input()))

num = sum(li) - 100
tag = 0

for i in range(8):
    if tag == 1:
        break
    for j in range(i+1, 9):
        if li[i] + li[j] == num:
            li.remove(li[j])
            li.remove(li[i])
            tag = 1
            break

for i in li:
    print(i)