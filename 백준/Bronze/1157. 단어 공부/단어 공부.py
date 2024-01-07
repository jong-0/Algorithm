abc = 'abcdefghijklmnopqrstuvwxyz'
s = input().lower()
li = [0]*26

for i in s:
    li[abc.index(i)] += 1

max = max(li)
cnt = li.count(max)

if cnt == 1:
    print(abc[li.index(max)].upper())
else:
    print('?')