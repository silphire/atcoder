aa = zip(list('ABC'), list(map(int, input().split())))
aa = sorted(aa, key=lambda x: x[1])
print(aa[1][0])