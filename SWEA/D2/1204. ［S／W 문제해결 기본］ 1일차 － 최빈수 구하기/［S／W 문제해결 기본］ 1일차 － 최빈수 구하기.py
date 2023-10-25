num = int(input())
for _ in range(num):
    n = int(input())
    chk = [0] * 101
    li = list(map(int, input().split()))
    for i in range(len(li)):
        chk[li[i]] += 1

    chk = chk[::-1]
    print('#'+str(n), 100 - chk.index(max(chk)))