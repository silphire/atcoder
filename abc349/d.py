l, r = map(int, input().split())

ans = []
while l < r:
    k = 1
    p = 2
    while l % p == 0 and p * (l // p + 1) <= r:
        k += 1
        p *= 2
    k -= 1
    p //= 2

    nl = p * (l // p + 1)
    ans.append((l, nl))
    l = nl

print(len(ans))
for a in ans:
    print(*a)