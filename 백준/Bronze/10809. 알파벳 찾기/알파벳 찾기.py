abc = 'abcdefghijklmnopqrstuvwxyz'
s = input()
li = [-1]*26

for i in s:
    li[abc.index(i)] = s.index(i)
print(*li)