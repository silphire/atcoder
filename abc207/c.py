n = int(input())
s = [None] * n
for i in range(n):
    t, l, r = map(int, input().split())
    s[i] = (l, r, t)
s.sort()
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if s[i][2] in (1, 2) and s[j][2] in (1, 3):
            f1 = s[i][0] <= s[j][1]
        else:
            f1 = s[i][0] < s[j][1]
        if s[j][2] in (1, 2) and s[i][2] in (1, 3):
            f2 = s[j][0] <= s[i][1]
        else:
            f2 = s[j][0] < s[i][1]
        if f1 and f2:
            ans += 1
print(ans)