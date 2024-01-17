s = input()
long = len(s)
c = long//2

front = s[:c]
if long%2 == 0:
    back = s[c:][::-1]
else:
    back = s[c+1:][::-1]

if front == back:
    print(1)
else:
    print(0)