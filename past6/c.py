n, m = map(int, input().split())
a = [0] * n
for i in range(n):
    _, *a[i] = map(int, input().split())
p, q = map(int, input().split())
b = set(map(int, input().split()))

ans = 0
for i in range(n):
    if len(set(a[i]) & b) >= q:
        ans += 1
print(ans) 