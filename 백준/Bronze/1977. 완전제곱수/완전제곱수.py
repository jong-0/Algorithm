import math

m = int(input())
n = int(input())

if (m**0.5)%1 == 0:
    mm = int(m**0.5)
else:
    mm = math.floor(m**0.5)+1

if (n**0.5)%1 == 0:
    nn = int(n**0.5)+1
else:
    nn = math.floor(n**0.5)+1

min = 0
sum = 0
for i in range(mm, nn):
    if min == 0:
        min += i ** 2

    sum += i**2

if min == 0:
    print(-1)
else:
    print(sum)
    print(min)