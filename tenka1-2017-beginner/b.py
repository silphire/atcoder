n = int(input())
amax = 0
bb = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a >= amax:
        amax = a
        bb = b
print(amax + bb)