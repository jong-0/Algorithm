abc = 'abcdefghijklmnopqrstuvwxyz'
li = [0] * 26
s = input()

for i in s:
    li[abc.index(i)] += 1

print(*li)