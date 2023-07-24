def divisors(n: int):
    """ 約数列挙
    """
    assert n >= 0

    import math

    divs_first = []
    divs_second = []
    for x in range(1, math.floor(n ** 0.5) + 1):
        if n % x == 0:
            divs_first.append(x)
            if x * x != n:
                divs_second.append(n // x)
    divs_first.extend(reversed(divs_second))
    return divs_first

for p in divisors(int(input())):
    print(p)