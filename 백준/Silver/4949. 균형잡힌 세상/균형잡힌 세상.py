while True:
    n = input()
    li = []
    flag = 0

    if n == '.':
        break

    for i in n:
        if i == '[' or i == '(':
            li.append(i)
        else:
            if i == ']':
                if li:
                    if li[-1] == '[':
                        li.pop()
                    else:
                        flag = 1
                        break
                else:
                    flag = 1
                    break
            elif i == ')':
                if li:
                    if li[-1] == '(':
                        li.pop()
                    else:
                        flag = 1
                        break
                else:
                    flag = 1
                    break
    if flag == 0:
        if len(li) == 0:
            print('yes')
        else:
            print('no')
    else:
        print('no')