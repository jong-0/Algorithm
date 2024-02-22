li = [0] * 5
for i in range(5):
    li[i] = int(input())

print(min(li[:3]) + min(li[3:]) - 50)