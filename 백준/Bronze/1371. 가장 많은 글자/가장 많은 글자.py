abc = 'abcdefghijklmnopqrstuvwxyz'
li = [0] * 26

while True:
    try:
        s = input().split()
        for i in s:
            for j in i:
                li[abc.index(j)] += 1
    except:
        break

m = max(li)
for i in range(26):
    if li[i] == m:
        print(abc[i], end = '')