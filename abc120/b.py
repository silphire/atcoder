a, b, k = map(int, input().split())
n = []
for x in range(1, min(a, b) + 1):
    if a % x == 0 and b % x == 0:
        n.append(x)
print(tuple(reversed(n))[k - 1])