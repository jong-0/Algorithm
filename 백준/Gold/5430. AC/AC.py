from collections import deque
import sys
input = sys.stdin.readline

num = int(input())

for _ in range(num):
    s = input()
    n = int(input())
    li = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    tag = 0
    cnt = 0

    if n == 0:
        li = deque()

    for i in s:
        if i == 'R':
            cnt += 1
        elif i == 'D':
            if li:
                if cnt%2 == 0:
                    li.popleft()
                else:
                    li.pop()
            else:
                tag = 1
                print('error')
                break
                
    if cnt%2 == 1:
        li.reverse()

    if tag == 0:
        print('[' + ','.join(li)+']')