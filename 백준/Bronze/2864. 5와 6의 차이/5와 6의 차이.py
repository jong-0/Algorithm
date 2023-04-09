import sys
input = sys.stdin.readline

a,b = input().split()

aa = a.replace('6', '5')
bb = b.replace('6', '5')

aaa = a.replace('5', '6')
bbb = b.replace('5', '6')

min = int(aa) + int(bb)
max = int(aaa) + int(bbb)

print(min, max)