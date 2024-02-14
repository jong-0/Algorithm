s = input().split('-')

if len(s) == 1:
    if '+' in s[0]:
        print(sum(list(map(int, s[0].split('+')))))
    else:
        print(int(s[0]))
else:
    if '+' in s[0]:
        ans = sum(list(map(int, s[0].split('+'))))
    else:
        ans = int(s[0])

    for i in range(1, len(s)):
        if '+' in s[i]:
            ans -= sum(list(map(int, s[i].split('+'))))
        else:
            ans -= int(s[i])

    print(ans)