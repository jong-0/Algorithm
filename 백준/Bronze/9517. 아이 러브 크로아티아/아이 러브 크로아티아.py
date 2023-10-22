idx = int(input())
num = int(input())
sec = 210

for i in range(num):
    a, b = input().split()
    sec -= int(a)
    if sec <= 0:
        print(idx)
        break

    if b == 'T':
        idx += 1
        if idx == 9:
            idx = 1
    else:
        continue