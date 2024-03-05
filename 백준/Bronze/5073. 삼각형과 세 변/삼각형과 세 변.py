while True:
    li = list(map(int, input().split()))
    if sum(li) == 0:
        break
    else:
        li.sort()
        if li[0] == li[1] and li[1] == li[2] and li[2] == li[0]:
            print('Equilateral')
        else:
            if li[0] + li[1] <= li[2]:
                print('Invalid')
            else:
                if li[0] == li[1] or li[1] == li[2]:
                    print('Isosceles')
                else:
                    print('Scalene')