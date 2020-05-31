from collections import Counter

n = int(input())

divisors = []
e = int(n ** 0.5) + 1
for a in range(2, e):
    while n % a == 0:
        divisors.append(a)
        n //= a
    if n == 1:
        break
if n != 1:
    divisors.append(n)

if len(divisors) == 0:
    print(0)
    exit(0)

ans = 0
ctr = Counter(divisors)
for d, n in ctr.items():
    x = 1
    while n >= x:
        n -= x
        x += 1
        ans += 1
print(ans)