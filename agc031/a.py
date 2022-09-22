from collections import Counter

MOD = 10 ** 9 + 7
n = int(input())
s = input().rstrip()
ctr = Counter(s)
ans = 1
for c, nc in ctr.items():
    ans *= nc + 1
    ans %= MOD
if ans == 0:
    ans = MOD - 1
else:
    ans -= 1
print(ans)