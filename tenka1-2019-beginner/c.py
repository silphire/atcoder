from collections import Counter
n = int(input())
s = list(input().rstrip())
c = Counter(s)
b = 0
w = c['.']
ans = w
for i in range(n):
    if s[i] == '#':
        b += 1
    else:
        w -= 1
    ans = min(ans, b + w)
print(ans)