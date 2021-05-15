aa = list(sorted(map(int, input().split())))
if aa[2] - aa[1] == aa[1] - aa[0]:
    print("Yes")
else:
    print("No")