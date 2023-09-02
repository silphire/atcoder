n, d, p = map(int, input().split())
ff = list(sorted(map(int, input().split()), reverse=True))
ans = sum(ff)
for i in range(0, n, d):
    a = sum(ff[i:i+d])
    if a < p:
        break
    ans = ans - a + p
print(ans)