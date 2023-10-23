n = int(input())

abc = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for _ in range(n):
    a, b = input().split()
    li = []
    for i in range(len(a)):
        ans = abc.index(b[i]) - abc.index(a[i])
        if ans < 0:
            ans += 26
        li.append(ans)
    print('Distances:', *li)