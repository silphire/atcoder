aa = list(map(int, input().split()))
if 1 <= min(aa) <= 9 and 1 <= max(aa) <= 9:
    print(aa[0] * aa[1])
else:
    print(-1)
    