n = int(input())
chk = 0

for i in range(1, n+1):
    n -= i
    if n < 1:
        chk = i
        break

x, y = 0, 0
if chk%2 == 0:
    x = (chk + n)
    y = chk + 1 - x
else:
    y = chk + n
    x = chk - y + 1

print(str(x) + '/' + str(y))