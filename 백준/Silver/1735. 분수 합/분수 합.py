a, b = map(int, input().split())
c, d = map(int, input().split())

x, y = a*d + b*c, b*d

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

a = max(x,y)
b = min(x,y)

print(x//gcd(a,b), y//gcd(a,b))