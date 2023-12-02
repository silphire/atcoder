mm, dd = map(int, input().split())
y, m, d = map(int, input().split())

d += 1
if d > dd:
    d -= dd
    m += 1
if m > mm:
    m -= mm
    y += 1

print(*[y, m, d])