x = int(input())
y = (x // 11) * 2
m = x % 11
if m > 6:
    y += 2
elif m > 0:
    y += 1
print(y)
