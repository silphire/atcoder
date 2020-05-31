n, m = map(int, input().split())
ans = None
for i in range(n):
    aa = tuple(map(int, input().split()))
    aa = aa[1:]
    if ans is None:
        ans = set(aa)
    else:
        ans = ans & set(aa)
print(len(ans))
