s = input()
li = []
while True:
    li.append(s)
    s=s[1:]
    if len(s) == 1:
        li.append(s)
        break

li.sort()
print(*li, sep='\n')