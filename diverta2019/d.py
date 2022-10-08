def divisors(n: int):
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

n = int(input())
dd = divisors(n)
ans = 0
for d in dd:
    if d == 1:
        continue
    m = d - 1
    if n // m == n % m:
        ans += m
print(ans)