for i in range(3):
    li = list(map(int, input().split()))
    n = sum(li)
    if n == 4:
        print('E')
    elif n == 3:
        print('A')
    elif n == 2:
        print('B')
    elif n == 1:
        print('C')
    else:
        print('D')