from collections import Counter
n = int(input())
aa = [a for a in sorted(Counter(map(int, input().split())).items(), key=lambda x: -x[0]) if a[1] >= 2]
if len(aa) >= 1 and aa[0][1] >= 4:
    print(aa[0][0] ** 2)
elif len(aa) >= 2:
    print(aa[0][0] * aa[1][0])
else:
    print(0)