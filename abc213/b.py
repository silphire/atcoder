n = int(input())
aa = list(map(int, input().split()))
aa = sorted([(a, i + 1) for i, a in enumerate(aa)])
print(aa[-2][1])