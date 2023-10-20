n = int(input())
tag = 0

for _ in range(n):
    s = input()
    if s == 'anj':
        tag = 1
        break

if tag == 1:
    print('뭐야;')
else:
    print('뭐야?')