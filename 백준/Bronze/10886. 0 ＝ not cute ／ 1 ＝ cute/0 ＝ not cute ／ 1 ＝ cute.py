n = int(input())
li = [0] * 2

for _ in range(n):
    li[int(input())] += 1

if li[0] > li[1]:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')