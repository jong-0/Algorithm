cnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
s = []

a = input()
b = input()

for i in range(len(a)):
    s.append(cnt[ord(a[i])-65])
    s.append(cnt[ord(b[i])-65])

chk = []
i, j = 0, 1
while len(s)!=2:
    max = len(s)-1
    chk.append((s[i]+s[j])%10)
    if j == max:
        i, j = 0, 1
        s = chk
        chk = []
    else:
        i += 1
        j += 1
print(str(s[0])+str(s[1]))