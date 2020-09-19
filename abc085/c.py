n, y = map(int, input().split())

y //= 1000

for a in range(0, n + 1):
    if a * 10 > y:
        break
    for b in range(0, n + 1):
        x = a * 10 + b * 5
        if x > y:
            break
        c = n - a - b
        if y == x + c:
            print(f"{a} {b} {c}")
            exit(0)
print("-1 -1 -1")