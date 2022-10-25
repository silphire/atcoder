n = int(input())
aa = list(map(int, input().split()))

x = None
for i in range(n - 1):
    if aa[i] > aa[i + 1]:
        x = aa[i]
        break
if x is None:
    x = aa[-1]

print(*[a for a in aa if a != x])