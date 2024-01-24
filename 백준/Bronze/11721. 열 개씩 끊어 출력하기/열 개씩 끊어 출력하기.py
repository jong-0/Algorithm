s = input()
chk = 1

for i in s:
    if chk != 10:
        print(i, end='')
        chk += 1
    else:
        print(i, end='\n')
        chk = 1