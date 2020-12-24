from collections import Counter
from collections import defaultdict

n = int(input())
ans = defaultdict(int)
for i in range(n):
    s = Counter(list(input().rstrip()))
    for k in 'abcdefghijklmnopqrstuvwxyz':
        if i > 0:
            ans[k] = min(ans[k], s[k])
        else:
            ans[k] = s[k]
s = ''
for k in sorted(ans.keys()):
    s += k * ans[k]
print(s)