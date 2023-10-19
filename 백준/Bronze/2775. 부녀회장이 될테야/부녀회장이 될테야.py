num = int(input())
for _ in range(num):
    a = int(input())
    b = int(input())

    li = [0] * b
    for i in range(b):
        li[i] = i + 1

    for i in range(a):
        for j in range(1, b):
            li[j] += li[j-1]

    print(li[b-1])