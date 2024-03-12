n = int(input())
li = [True] * (int(n**0.5)+1)

for i in range(2, int(n**0.5)+1):
    if i == False:
        continue
    for j in range(i+i, int(n**0.5)+1, i):
        li[j] = False

for i in range(2, len(li)):
    if li[i]:
        while n%i == 0:
            n //= i
            print(i)

if n != 1:
    print(n)