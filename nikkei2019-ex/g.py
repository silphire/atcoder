from collections import Counter

s = Counter(list(input().rstrip()))
odd = 0
ans = 0
for k, n in s.items():
    if n % 2 == 0:
        ans += n
    else:
        ans += n - 1
        odd += 1
if odd > 0:
    odd -= 1
    ans += 1
print(ans * ans + odd)
