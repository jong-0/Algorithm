num = int(input())
n = list(map(int, input().split()))
cc = int(input())

n.sort()

cnt = 0

i = 0
j = len(n) - 1

while i < j:
    s = n[i] + n[j]
    if s == cc:
        cnt += 1
        i += 1
        j -= 1
    elif s < cc:
        i += 1
    else:
        j -= 1

print(cnt)