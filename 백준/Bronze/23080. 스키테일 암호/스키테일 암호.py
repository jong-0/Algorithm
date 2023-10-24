n = int(input())
s = input()
cnt = 0
for i in s:
    if cnt%n == 0:
        print(i, end='')
    cnt+=1