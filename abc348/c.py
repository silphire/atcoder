n = int(input())
aa = {}
for i in range(n):
    a, c = map(int, input().split())
    if c in aa:
        aa[c] = min(aa[c], a)
    else:
        aa[c] = a
print(max(aa.values()))