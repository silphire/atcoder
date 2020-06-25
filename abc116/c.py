n = int(input())
hh = tuple(map(int, input().split()))
h = [0] * n

prev = 0
ans = 0
while True:
    x = 0
    y = 0
    while x < n:
        if h[x] == hh[x]:
            x += 1
            continue

        ansadd = hh[x] - h[x]
        y = x + 1
        while y < n and h[y] < hh[y]:
            ansadd = min(ansadd, hh[y] - h[y])
            y += 1
        for i in range(x, y):
            h[i] += ansadd
        ans += ansadd

    if ans == prev:
        break
    prev = ans
print(ans)
