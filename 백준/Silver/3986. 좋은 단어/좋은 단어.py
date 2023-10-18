num = int(input())
cnt = 0

for _ in range(num):
    s = input()

    if len(s)%2 != 0:
        continue
    else:
        li = []

        for i in s:
            if len(li) == 0:
                li.append(i)
            else:
                if i == 'A':
                    if li and li[-1] == 'A':
                        li.pop()
                    else:
                        li.append(i)
                else:
                    if li and li[-1] == 'B':
                        li.pop()
                    else:
                        li.append(i)

    if len(li) == 0:
        cnt += 1

print(cnt)