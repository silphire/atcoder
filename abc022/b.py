from collections import Counter
n = int(input())
a = [int(input()) for _ in range(n)]
ans = 0
for _, x in Counter(a).items():
    ans += x - 1
print(ans)