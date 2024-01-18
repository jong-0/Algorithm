li = []
for _ in range(9):
    li.append(list(map(int,input().split())))

ii = 1
jj = 1
max = 0
for i in range(9):
    for j in range(9):
        if li[i][j] > max:
            max = li[i][j]
            ii = i + 1
            jj = j + 1

print(max)
print(ii, jj)