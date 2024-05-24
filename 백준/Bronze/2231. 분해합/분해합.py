n = int(input())
tag = 0
for i in range(1, n+1):
    if n == i + sum(map(int, str(i))):
        print(i)
        tag = 1
        break

if tag == 0:
    print(0)