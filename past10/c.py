alpha = int(input())
x = 0
while alpha >= 1000:
    alpha //= 1000
    x += 1
x -= 1
print(str(alpha) + chr(ord('a') + x))