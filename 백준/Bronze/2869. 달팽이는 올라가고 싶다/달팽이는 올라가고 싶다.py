a,b,v = map(int, input().split())

if a >= v:
    print(1)
else:
    if (v - a) >= (a - b):
        if (v-a)%(a-b) == 0:
            print(1 + (v - a) // (a - b))
        else:
            print(1 + (v - a) // (a - b) + 1)
    else:
        print(2)
