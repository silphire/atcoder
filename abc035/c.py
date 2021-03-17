n, q = map(int, input().split())
a = [0] * (n + 1)
for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    a[l] += 1
    a[r + 1] -= 1
for i in range(1, n + 1):
    a[i] += a[i - 1]
print(''.join([str(a[i] % 2) for i in range(0, n)]))