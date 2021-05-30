n, k = map(int, input().split())
d = [tuple(map(int, input().split())) for _ in range(n)]
d.sort()

p = 0
for i in range(n):
    if p + k >= d[i][0]:
        k -= d[i][0] - p
        k += d[i][1]
        p = d[i][0]
    else:
        p += k
        k = 0
        break
print(p + k)