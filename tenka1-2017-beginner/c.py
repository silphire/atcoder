N = int(input())
for h in range(1, 3501):
    for w in range(1, 3501):
        d = (4.0 * h * w - N * h - N * w)
        if abs(d) < 1e-6:
            continue
        n = (N * h * w) / d
        if n <= 0:
            continue
        if abs(n - int(n)) < 1e-6:
            print(f'{h} {int(n)} {w}')
            exit()