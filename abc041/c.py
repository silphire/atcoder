n = int(input())
aa = sorted([(-a, i + 1) for i, a in enumerate(map(int, input().split()))])
for a in aa:
    print(a[1])
