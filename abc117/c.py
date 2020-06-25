n, k = map(int, input().split())
pp = tuple(sorted(map(int, input().split())))

if n >= k:
    print(0)
    exit(0)

intv = []
for i in range(1, len(pp)):
    intv.append(pp[i] - pp[i - 1])
intv = sorted(intv)

ans = pp[-1] - pp[0]
for i in range(n - 1):
    ans -= intv[-i - 1]
print(ans)