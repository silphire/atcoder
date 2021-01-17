sx, sy, tx, ty = map(int, input().split())
x = tx - sx
y = ty - sy
ans = ''

ans += 'R' * x
ans += 'U' * y

ans += 'R'
ans += 'D' * (y + 1)
ans += 'L' * (x + 1)
ans += 'U'

ans += 'U' * y
ans += 'R' * x

ans += 'U'
ans += 'L' * (x + 1)

ans += 'D' * (y + 1)
ans += 'R'

print(ans)