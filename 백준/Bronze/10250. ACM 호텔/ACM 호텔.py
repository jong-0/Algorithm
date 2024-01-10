num = int(input())
for _ in range(num):
    h, w, n = map(int, input().split())

    if n == 1:
        floor = 1
        room = 1
    else:
        room = n//h + 1
        floor = n%h
        if n%h == 0:
            floor = h
            room = n//h

    if room < 10:
        room = '0'+str(room)
    print(str(floor) + str(room))