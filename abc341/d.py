import math

n, m, k = map(int, input().split())

l = math.lcm(n, m)
left = 0
right = 2 ** 63
while left + 1 < right:
    mid = (left + right) // 2
    km = (mid // n) + (mid // m) - 2 * (mid // l)
    if km < k:
        left = mid
    else:
        right = mid
print(right)
