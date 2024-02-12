import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
chk = list(map(int, input().split()))

def bubble(li, chk):
    for i in range(n-1):
        tag = False
        for j in range(n-i-1):
            if li[j] > li[j+1]:
                tag = True
                li[j], li[j + 1] = li[j + 1], li[j]
                if li[j] == chk[j]:
                    if chk == li:
                        print(1)
                        sys.exit(0)
        if not tag:
            break
    print(0)

if li == chk:
    print(1)
    sys.exit(0)
else:
    bubble(li, chk)