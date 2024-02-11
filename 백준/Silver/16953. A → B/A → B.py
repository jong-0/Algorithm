a, b = map(int, input().split())
cnt = 0
tag = 1

while True:
    tag = -1

    if b%10 == 1:
        b = b//10
        cnt += 1
        tag = 1
    elif b%2 == 0:
        b = b//2
        cnt += 1
        tag = 1
    if b == 0:
        tag = -1
        break
    if b == a:
        break
    if tag == -1:
        break
if tag == 1:
    print(cnt+1)
else:
    print(-1)