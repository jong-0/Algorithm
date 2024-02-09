a, b = input().split()

if '5' in a:
    max_a = a.replace('5', '6')
else:
    max_a = a
if '6' in a:
    min_a = a.replace('6', '5')
else:
    min_a = a
if '5' in b:
    max_b = b.replace('5', '6')
else:
    max_b = b
if '6' in b:
    min_b = b.replace('6', '5')
else:
    min_b = b
print(int(min_a)+int(min_b), int(max_a)+int(max_b))