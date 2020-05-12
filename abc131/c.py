from fractions import gcd

global a, b, c, d
a, b, c, d = map(int, input().split())

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solve(n):
    x = n // c
    y = n // d
    z = n // lcm(c, d)
    return n - x - y + z

print(solve(b) - solve(a - 1))