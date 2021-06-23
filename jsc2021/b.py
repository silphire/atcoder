n, m = map(int, input().split())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))
cc = []

i = 0
j = 0
while i < n and j < m:
    if aa[i] == bb[j]:
        i += 1
        j += 1
    elif aa[i] < bb[j]:
        cc.append(aa[i])
        i += 1
    elif aa[i] > bb[j]:
        cc.append(bb[j])
        j += 1
while i < n:
    cc.append(aa[i])
    i += 1
while j < m:
    cc.append(bb[j])
    j += 1
print(' '.join(map(str, cc)))