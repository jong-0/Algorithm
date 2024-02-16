li = [0] * 10
s = input()
for i in s:
    li[int(i)] += 1

li[6] += li[9]
if li[6]%2 == 0:
    li[6] = li[6]//2
else:
    li[6] = (li[6]+1) // 2

print(max(li[:9]))