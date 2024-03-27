abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input())
for _ in range(n):
    a, b = input().split()
    print('Distances:', end = ' ')
    for i in range(len(a)):
        dist = abc.index(b[i]) - abc.index(a[i])
        if dist < 0:
            dist += 26
        print(dist, end = ' ')
    print()