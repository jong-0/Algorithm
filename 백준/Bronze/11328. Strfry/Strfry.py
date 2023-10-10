import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    aa, bb = input().split()
    aa1 = sorted(aa)
    bb1 = sorted(bb)

    if aa1 == bb1:
        print("Possible")
    else:
        print("Impossible")