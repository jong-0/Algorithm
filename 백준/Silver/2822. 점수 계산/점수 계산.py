li = [0] * 8
for i in range(8):
    li[i] = int(input())

chk = sorted(li)
ans = chk[3:]
ll = []
print(sum(ans))
for i in ans:
    ll.append(li.index(i)+1)

ll.sort()
print(*ll)