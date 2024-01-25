aa = [0] * 3
bb = [0] * 3

for i in range(3):
    a, b = map(int, input().split())
    aa[i] = a
    bb[i] =b

aa.sort()
bb.sort()


if aa[1] == aa[0]:
    print(aa[2], end=' ')
else:
    print(aa[0], end=' ')

if bb[1] == bb[0]:
    print(bb[2])
else:
    print(bb[0])