s = input()
li = []
ans = 0

for i in range(len(s)):
    if s[i] == '(':
        li.append(s[i])
    else:
        if s[i-1] == '(':
            li.pop()
            ans += len(li)
        else:
            li.pop()
            ans += 1

print(ans)