import itertools

n = int(input())
aa = list(map(int, input().split()))

tri = []
stri = set()
for x in itertools.combinations(range(n * 3), 3):
    if aa[x[0]] < aa[x[1]] + aa[x[2]] and aa[x[1]] < aa[x[0]] + aa[x[2]] and aa[x[2]] < aa[x[0]] + aa[x[1]]:
        tri.append(set(x))
        stri.add(x)

ans = 0
for x in itertools.combinations(range(len(tri)), n - 1):
    s = set()
    for i in x:
        s |= tri[i]
    if len(s) != 3 * (n - 1):
        continue
    v = tuple(sorted(set(range(3 * n)) - s))
    if v in stri:
        ans += 1
print(ans // n)