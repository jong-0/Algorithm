while True:
    n = input()
    if int(n) == 0:
        break
    else:
        ll = len(n)
        if ll%2 == 0:
            front = n[:ll//2]
            back = n[ll//2:][::-1]
        else:
            front = n[:ll//2]
            back = n[ll//2+1:][::-1]

    if front == back:
        print('yes')
    else:
        print('no')