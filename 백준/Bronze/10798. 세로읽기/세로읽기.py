li = []

for i in range(5):
    li.append(list(input()))

for i in range(15):
    for j in range(5):
        if i < len(li[j]):
            print(li[j][i], end='')