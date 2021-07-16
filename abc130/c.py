w, h, x, y = map(int, input().split())
print(f'{w * h / 2} {int(x + x == w and y + y == h)}')