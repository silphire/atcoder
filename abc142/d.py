import math

def divisors(n):
    s = set()
    for x in range(2, math.ceil(n ** 0.5) + 1):
        while n % x == 0:
            s.add(x)
            n /= x
            if n == 1:
                break
    if n > 1:
        s.add(n)
    return s
 
a, b = map(int, input().split())
d = divisors(a) & divisors(b)
print(len(d) + 1)