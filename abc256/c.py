h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0
for a11 in range(1, 31):
    for a12 in range(1, 31):
        for a21 in range(1, 31):
            for a22 in range(1, 31):
                a13 = h1 - a11 - a12
                a23 = h2 - a21 - a22
                if a13 < 1 or a23 < 1:
                    continue

                a31 = w1 - a11 - a21
                a32 = w2 - a12 - a22
                if a31 < 1 or a32 < 1:
                    continue

                a33a = h3 - a31 - a32
                a33b = w3 - a13 - a23
                if a33a != a33b or a33a < 1 or a33b < 1:
                    continue

                ans += 1
print(ans)