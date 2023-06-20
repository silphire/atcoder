def lcm(a: int, b: int) -> int:
    import math

    return a * b // math.gcd(a, b)

print(lcm(*map(int, input().split())))