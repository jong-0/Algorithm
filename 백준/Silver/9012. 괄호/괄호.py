num = int(input())
for _ in range(num):
    s = input()
    li = []
    flag = 0

    for i in s:
        if i == '(':
            li.append(i)
        else:
            if li and li[-1] == '(':
                li.pop()
            else:
                flag = 1
                break
    if flag == 0 and len(li) == 0:
        print('YES')
    else:
        print('NO')