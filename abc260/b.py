n, x, y, z = map(int, input().split())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

st = sorted([i for i in range(n)], key=lambda j: (-aa[j], j))
ans = st[:x]

st = sorted(st[x:], key=lambda j: (-bb[j], j))
ans += st[:y]

st = sorted(st[y:], key=lambda j: (-aa[j] - bb[j], j))
ans += st[:z]

for s in sorted(ans):
    print(s + 1)
