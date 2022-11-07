n, k = map(int, input().split())
k2 = int(str(k)[::-1])
if k != min(k, k2):
    print(0)
    exit()

f = k == k2
ans = 0
while k <= n:
    ans += 1
    k *= 10
while k2 <= n:
    ans += 1
    k2 *= 10
if f:
    ans //= 2
print(ans)