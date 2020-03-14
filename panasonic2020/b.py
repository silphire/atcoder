import math
h, w = map(int, input().split())

ans = 0
if h == 1 or w == 1:
    ans = 1
elif h % 2 == 1 and w % 2 == 1:
    ans = (h - 1) * w // 2 + (w + 1) // 2
else:
    ans = h * w // 2
print(ans)
