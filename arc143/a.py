aa = sorted(map(int, input().split()))
if aa[0] + aa[1] >= aa[2]:
    print(aa[2])
else:
    print(-1)