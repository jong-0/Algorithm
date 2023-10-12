num = int(input())

for _ in range(num):
    pwd = input()
    l = []
    r = []

    for i in pwd:
        if i == '<':
            if l:
                r.append(l.pop())
        elif i == '>':
            if r:
                l.append(r.pop())
        elif i == '-':
            if l:
                l.pop()
        else:
            l.append(i)
            
    l.extend(reversed(r))
    print(''.join(l))