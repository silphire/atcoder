n = int(input())

mf = float('inf')
b = 10 ** 6
for a in range(0, 10 ** 6 + 1):
    while b >= 0:
        f = a ** 3 + a * a * b + a * b * b + b ** 3
        if f < n:
            break
        mf = min(mf, f)
        b -= 1
print(mf)