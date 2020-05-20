n, q = map(int, input().split())
s = input().rstrip()

ns = [None] * n
ns[0] = 0
nn = 0
for i in range(n - 1):
    if s[i] == 'A' and s[i + 1] == 'C':
        nn += 1
    ns[i + 1] = nn
for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1

    print(ns[r] - ns[l])