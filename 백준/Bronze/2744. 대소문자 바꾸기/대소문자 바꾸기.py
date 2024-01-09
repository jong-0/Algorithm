abc = 'abcdefghijklmnopqrstuvwxyz'
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = []

s = input()
for i in s:
    if i in abc:
        ans.append(ABC[abc.index(i)])
    else:
        ans.append(abc[ABC.index(i)])

print(*ans, sep='')