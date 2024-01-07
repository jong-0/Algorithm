num = int(input())
for i in range(num):
    a,b = input().split()
    for j in b:
        print(j*int(a), end='')
    print()