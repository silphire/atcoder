import math

def divisors(n: int) -> list[int]:
    divs_first = []
    divs_second = []
    for x in range(1, math.floor(n ** 0.5) + 1):
        if n % x == 0:
            divs_first.append(x)
            if x * x != n:
                divs_second.append(n // x)
    divs_first.extend(reversed(divs_second))
    return divs_first


n, k = map(int, input().split())
aa = list(map(int, input().split()))

ans = []
diff = [aa[i] - aa[i - 1] for i in range(1, k)]
ds = divisors(math.gcd(*diff))
for d in ds:
    if 1 + (aa[-1] - aa[0]) / d <= n:
        ans.append(d)

print(len(ans))
print(*ans)
