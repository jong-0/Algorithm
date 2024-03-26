ae = 'aeiou'

while True:
    s = input()
    if s == '#':
        break
    else:
        cnt = 0
        s = s.lower()
        for i in s:
            if i in ae:
                cnt += 1
    print(cnt)