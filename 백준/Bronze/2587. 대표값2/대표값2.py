li = [0] * 5
for i in range(5):
    li[i] = int(input())

li.sort()

print(int(sum(li)/5))
print(li[2])