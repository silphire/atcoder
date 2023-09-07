n = int(input())
aa = list(map(int, input().split()))

bb = [0] * n
ar = sorted([(a, i) for i, a in enumerate(aa)])
for i, a in enumerate(ar):
    bb[a[1]] = i + 1
print(*bb)