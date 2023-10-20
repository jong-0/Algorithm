a, aa = map(int,input().split())
b, bb = map(int,input().split())

while aa > 0 and bb > 0:
    aa -= b
    bb -= a

if aa <= 0 and bb <= 0:
    print('DRAW')
elif aa > 0 and bb <= 0:
    print('PLAYER A')
else:
    print('PLAYER B')