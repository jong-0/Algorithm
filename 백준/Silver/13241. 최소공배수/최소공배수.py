def GCD(a,b):
    if a%b == 0:
        return b
    else:
        return GCD(b, a%b)

aa, bb = map(int, input().split())
a = max(aa, bb)
b = min(aa, bb)

gcd = GCD(a,b)
print(gcd * aa//gcd * bb//gcd)