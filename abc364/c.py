n, x, y = map(int, input().split())
aa = list(sorted(map(int, input().split()), reverse=True))
bb = list(sorted(map(int, input().split()), reverse=True))

a = 0
b = 0
for i in range(n):
    a += aa[i]
    b += bb[i]
    if a > x or b > y:
        break

print(i + 1)