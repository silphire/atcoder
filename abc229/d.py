s = input().rstrip()
k = int(input())
n = len(s)
w = [0] * (n + 1)
for i in range(n):
    if s[i] == '.':
        w[i + 1] = w[i] + 1
    else:
        w[i + 1] = w[i]

ans = 0
r = 0
for l in range(n):
    while r < n and w[r + 1] - w[l] <= k:
        r += 1
    ans = max(ans, r - l)
print(ans)