n = int(input())
sum = 0

for _ in range(n):
    s = input()
    ans = len(set(s))
    cnt = 1
    chk = s[0]

    for i in range(1,len(s)):
        if chk == s[i]:
            continue
        else:
            cnt += 1
            chk = s[i]

    if ans == cnt:
        sum += 1

print(sum)