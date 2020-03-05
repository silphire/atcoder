n, k = map(int, input().split())
h = map(int, input().split())
h = list(sorted(h))
if k > 0:
    print(sum(h[:-k]))
else:
    print(sum(h))