n, m = map(int, input().split())
s = set([x for x in range(1, n + 1)])
for _ in range(m):
    a, b = map(int, input().split())
    s.discard(b)
if len(s) == 1:
    print(list(s)[0])
else:
    print(-1)