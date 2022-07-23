l1, r1, l2, r2 = map(int, input().split())
a = [0] * 101
a[l1] += 1
a[r1] -= 1
a[l2] += 1
a[r2] -= 1
for i in range(100):
    a[i + 1] += a[i]

x = 0
for i in range(100):
    if a[i] == 2:
        x += 1
print(x)
