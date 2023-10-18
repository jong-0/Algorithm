score = [100, 100, 200, 200, 300, 300, 400, 400, 500]

li = list(map(int, input().split()))
tag = 0

for i in range(len(li)):
    if li[i] > score[i]:
        tag = 1

if tag == 1:
    print('hacker')
else:
    if sum(li) < 100:
        print('none')
    else:
        print('draw')