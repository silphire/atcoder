aa = list(sorted(map(int, input().split())))
print(['No', 'Yes'][int(aa[0] + aa[1] == aa[2])])