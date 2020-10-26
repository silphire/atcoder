aa = list(sorted(input().split()))
if aa[0] == aa[1]:
    print(aa[2])
elif aa[0] == aa[2]:
    print(aa[1])
else:
    print(aa[0])