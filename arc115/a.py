from collections import Counter

n, m = map(int, input().split())
ss = [
    Counter(input().rstrip())['1']
    for _ in range(n)
]
odd = [0] * n
for i in range(n - 1, -1, -1):
    odd[i] = ss[i] & 1
    if i + 1 < n:
        odd[i] += odd[i + 1]
ans = 0
for i in range(n):
    if ss[i] & 1 == 0:
        ans += odd[i]
    else:
        ans += (n - i) - odd[i]
print(ans)