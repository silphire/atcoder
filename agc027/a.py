n, x = map(int, input().split())
aa = list(sorted(map(int, input().split())))

ans = 0
for a in aa:
    x -= a
    if x < 0:
        break
    ans += 1
if x > 0:
    ans -= 1
print(ans)