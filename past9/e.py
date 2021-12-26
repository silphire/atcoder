n = input().rstrip()
f = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
ans = 0
for i, c in enumerate(n):
    if i == 0:
        ans += 500
    elif c == n[i - 1]:
        ans += 301
    elif f[int(c)] == f[int(n[i - 1])]:
        ans += 210
    else:
        ans += 100
print(ans)
