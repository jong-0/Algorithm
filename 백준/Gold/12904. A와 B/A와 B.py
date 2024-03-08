s = input()
t = input()

while True:
    if s == t:
        print(1)
        break
    else:
        if t[-1] == 'A':
            t = t[:-1]
        else:
            t = t[:-1][::-1]

    if len(s)>len(t):
        print(0)
        break