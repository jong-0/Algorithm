li = [0] * 9

r = input()

for i in r:
    if i == '9':
        li[int(6)] += 1
    else:
        li[int(i)] += 1

if li[6]%2 == 0:
    li[6] = li[6]/2
else:
    li[6] = (li[6]+1)/2

print(int(max(li)))