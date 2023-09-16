s = input()
n = len(s)
ans = 1
for i in range(n):
    for j in range(i, n):
        a, b = i, j
        x = b - a + 1
        while a < b:
            if s[a] != s[b]:
                x = 0
                break
            a += 1
            b -= 1
        ans = max(ans, x)
print(ans)