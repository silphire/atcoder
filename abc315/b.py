m = int(input())
dd = list(map(int, input().split()))
mid = (sum(dd) + 1) // 2
ad = 0
for i in range(m):
    for j in range(dd[i]):
        ad += 1
        if ad == mid:
            print(*[i + 1, j + 1])
            exit()