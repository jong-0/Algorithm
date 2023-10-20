num = int(input())
li = list(map(int, input().split()))
cnt = 0
max = 0
for i in range(num):
    if li[i] != 0:
        cnt+=1
    if li[i] == 0:
        if cnt > max:
            max = cnt
        cnt = 0
if cnt > max:
    max = cnt
print(max)