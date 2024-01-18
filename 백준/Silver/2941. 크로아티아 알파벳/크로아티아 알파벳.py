li = ['dz=','c=','c-','d-','lj','nj','s=','z=']
s = input()
idx = 0
cnt = 0

while True:
    if li[idx] in s:
        cnt += s.count(li[idx])
        s = s.replace(li[idx],' ')
    else:
        if idx < len(li) - 1:
            idx += 1
        else:
            break

s = s.replace(' ','')
print(cnt + len(s))